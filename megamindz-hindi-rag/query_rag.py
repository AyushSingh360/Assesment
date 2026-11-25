import os
import time
from pathlib import Path
import chromadb
from google import genai
from google.genai import errors
from sentence_transformers import SentenceTransformer

DB_DIR = Path("./chroma_db")
COLLECTION_NAME = "agni_hindi_rag"
EMBED_MODEL = "BAAI/bge-m3"
CANDIDATE_MODELS = ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.6-flash", "gemini-3.5-flash"]
TOP_K = 5

TEST_QUERIES = [
    ("HI", "SLV-III ने किस उपग्रह को कक्षा में स्थापित किया और किस वर्ष?"),
    ("HI", "कलाम को भारत रत्न किस वर्ष प्राप्त हुआ?"),
    ("HI", "पोखरण-II में कलाम की क्या भूमिका थी?"),
    ("EN", "Which institution did Kalam attend to study aeronautical engineering?"),
    ("EN", "Who co-wrote the autobiography, and in what year was it published?"),
    ("EN", "How and where did Kalam die in 2015?"),
]


def format_context(results: dict) -> tuple[str, list[dict]]:
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]

    blocks = []
    citations = []
    for doc_text, meta, dist in zip(docs, metas, dists):
        score = round(max(0.0, 1.0 - float(dist)), 4)
        cite_obj = {
            "page": meta.get("page"),
            "section": meta.get("section"),
            "chunk_id": meta.get("chunk_id"),
            "score": score,
        }
        citations.append(cite_obj)
        blocks.append(
            f"[chunk_id: {cite_obj['chunk_id']} | page: {cite_obj['page']} | section: \"{cite_obj['section']}\" | score: {score}]\n{doc_text}"
        )
    return "\n\n---\n\n".join(blocks), citations


def generate_with_retry(genai_client: genai.Client, prompt: str) -> tuple[str, str]:
    last_err = None
    for model_name in CANDIDATE_MODELS:
        for attempt in range(1, 5):
            try:
                response = genai_client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                return (response.text or "").strip(), model_name
            except errors.ServerError as e:
                last_err = e
                wait = attempt * 4
                print(f"[{model_name}] 503 busy (attempt {attempt}/4), retrying in {wait}s...")
                time.sleep(wait)
            except errors.ClientError as e:
                last_err = e
                break  # model not enabled for this key; move to next candidate
    raise RuntimeError(f"All candidate Gemini models failed: {last_err}")


def answer_query(
    query: str,
    collection,
    embed_model: SentenceTransformer,
    genai_client: genai.Client,
    top_k: int = TOP_K,
) -> tuple[str, list[dict], str]:
    q_emb = embed_model.encode([query], normalize_embeddings=True).tolist()
    results = collection.query(
        query_embeddings=q_emb,
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    context_str, citations = format_context(results)

    prompt = f"""You are a strictly grounded RAG assistant. Answer the user's question using ONLY the provided context chunks from the Hindi reference document.
Do NOT use outside knowledge or guess. If the context does not contain the answer, state that clearly.

Question: {query}

Retrieved Context:
{context_str}
"""
    text, used_model = generate_with_retry(genai_client, prompt)
    return text, citations, used_model


def main() -> None:
    if not os.environ.get("GEMINI_API_KEY"):
        raise EnvironmentError("Set GEMINI_API_KEY in PowerShell before running query_rag.py")

    embed_model = SentenceTransformer(EMBED_MODEL)
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_collection(COLLECTION_NAME)
    genai_client = genai.Client()

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    report_lines = ["# MegaMindz Level 1 RAG — Test Query Results\n"]

    for idx, (lang, query) in enumerate(TEST_QUERIES, start=1):
        answer, citations, used_model = answer_query(query, collection, embed_model, genai_client)
        top_cite = citations[0] if citations else {}

        block = [
            f"## Query {idx} ({lang})",
            f"- **Query:** {query}",
            f"- **Answer:** {answer}",
            f"- **Model:** {used_model}",
            f"- **Primary Citation:** page: {top_cite.get('page')}, section: \"{top_cite.get('section')}\", chunk_id: {top_cite.get('chunk_id')}, score: {top_cite.get('score')}",
            "- **All Retrieved Chunks:**",
        ]
        for c in citations:
            block.append(
                f"  - page: {c['page']} | section: \"{c['section']}\" | chunk_id: {c['chunk_id']} | score: {c['score']}"
            )
        rendered = "\n".join(block) + "\n"
        print(rendered)
        report_lines.append(rendered)
        time.sleep(1.5)

    out_path = out_dir / "results.md"
    out_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Saved full results to {out_path}")


if __name__ == "__main__":
    main()
