import re
import unicodedata
from pathlib import Path
import fitz
import chromadb
from sentence_transformers import SentenceTransformer

PDF_PATH = Path("data/Agni_Ki_Udaan_Adhyayan_Sahayika_Hindi.pdf")
DB_DIR = Path("./chroma_db")
COLLECTION_NAME = "agni_hindi_rag"
EMBED_MODEL = "BAAI/bge-m3"


def normalize_hindi(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[^\S\n]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_hindi_chunks(text: str, max_chars: int = 480, overlap_chars: int = 80) -> list[str]:
    units = re.split(r"(?<=[।?!\n])\s+", text)
    chunks: list[str] = []
    current = ""

    for raw_unit in units:
        unit = raw_unit.strip()
        if not unit:
            continue

        if len(unit) > max_chars:
            if current:
                chunks.append(current)
                current = ""
            for i in range(0, len(unit), max_chars - overlap_chars):
                part = unit[i : i + max_chars].strip()
                if part:
                    chunks.append(part)
            continue

        candidate = f"{current} {unit}".strip() if current else unit
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current)
            tail = current[-overlap_chars:].strip() if (current and overlap_chars > 0) else ""
            current = f"{tail} {unit}".strip() if tail else unit

    if current:
        chunks.append(current)
    return chunks


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Missing PDF at {PDF_PATH}")

    doc = fitz.open(str(PDF_PATH))
    model = SentenceTransformer(EMBED_MODEL)

    client = chromadb.PersistentClient(path=str(DB_DIR))
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    ids: list[str] = []
    documents: list[str] = []
    metadatas: list[dict] = []

    current_section = "शीर्षक / भूमिका"
    chunk_counter = 0

    for page_num, page in enumerate(doc, start=1):
        raw_page_text = normalize_hindi(page.get_text("text"))
        if not raw_page_text:
            continue

        for line in raw_page_text.splitlines():
            s = line.strip()
            if re.match(r"^(\d{1,2})\s*[.•\-–—:]\s*.+", s) and len(s) <= 95:
                current_section = s

        for chunk in split_hindi_chunks(raw_page_text):
            chunk_counter += 1
            chunk_id = f"chunk_{chunk_counter:04d}"
            ids.append(chunk_id)
            documents.append(chunk)
            metadatas.append(
                {
                    "chunk_id": chunk_id,
                    "page": page_num,
                    "section": current_section,
                    "source_doc": PDF_PATH.name,
                }
            )

    embeddings = model.encode(
        documents,
        batch_size=32,
        normalize_embeddings=True,
        show_progress_bar=True,
    ).tolist()

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    print(f"Ingested {len(ids)} chunks from {len(doc)} pages into '{COLLECTION_NAME}' at {DB_DIR}.")


if __name__ == "__main__":
    main()
