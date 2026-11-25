# Cross-Lingual Hindi RAG Pipeline (MegaMindz AI Solutions - Level 1)

## 1. Chunking Strategy
Sentence- and punctuation-aware splitting on Hindi danda (।), ?, !, and newlines (480 chars target, 80 chars overlap) to preserve Devanagari clauses and cross-boundary context.

## 2. Vector Database Choice
ChromaDB (persistent local storage) for zero-daemon local execution, HNSW cosine similarity, and automatic metadata persistence (page, section, chunk_id, source_doc).

## 3. Hindi Text & Cross-Lingual Handling
UTF-8 extraction with NFC Unicode normalization, BAAI/bge-m3 cross-lingual (EN -> HI) embeddings, and Gemini answer generation with automatic metadata citations.

## 4. Limitations & Next Steps
Heading regex can match numbered list/question lines; tightening heading detection, adding structured table extraction, and evaluating top-k retrieval on Section 19 questions are next steps.

## 5. How to Run
1. Create/activate venv: python -m venv .venv; .\.venv\Scripts\Activate.ps1
2. Install deps: pip install -r .\requirements.txt
3. Set UTF-8 and API key: [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $env:PYTHONUTF8 = '1'; $env:GEMINI_API_KEY='your_api_key'
4. Run: python .\ingest.py; python -u .\query_rag.py
