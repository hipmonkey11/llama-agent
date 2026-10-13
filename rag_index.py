import os
import glob
from typing import List
import chromadb
from sentence_transformers import SentenceTransformer

from config import CHROMA_DIR, KB_DIR, MAX_TOKENS_PER_CHUNK, CHUNK_OVERLAP

def read_markdown_files(folder: str) -> List[str]:
    paths = sorted(glob.glob(os.path.join(folder, "**", "*md"), recursive=True))
    docs = []
    for p in paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                docs.append((p, f.read()))
        except Exception as e:
            print(f"[WARN] Skipped {p}: {e}")
    return docs

def simple_chunk(text: str, max_chars: int = 1800, overlap: int = 200) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        if end == len(text):
            break
        start = end - overlap
        if start < 0:
            start = 0
    return chunks

def main():
    os.makedirs(CHROMA_DIR, exist_ok=True)
    docs = read_markdown_files(KB_DIR)
    if not docs:
        print(f"[ERROR] No Markdown files found in {KB_DIR}/")
        return
    
    print(f"[INFO] Loaded {len(docs)} documents from {KB_DIR}/")

    print("[INFO] Loading embedding model: BAAI/bge-small-en")
    embedder = SentenceTransformer("BAAI/bge-small-en")

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_or_create_collection("codex")

    try:
        ids = collection.get()["ids"]
        if ids:
            print(f"[INFO] Clearing existing {len(ids)} vectors...")
            collection.delete(ids)
    except Exception:
        pass

    total_chunks = 0
    for path, text in docs:
        chunks = simple_chunk(text, max_chars=MAX_TOKENS_PER_CHUNK*4, overlap=CHUNK_OVERLAP*4)
        meta_source = os.path.relpath(path, KB_DIR)

        for i, ch in enumerate(chunks):
            vec = embedder.encode(ch).tolist()
            uid = f"{meta_source}#{i}"
            collection.add(ids=[uid], embeddings=[vec], documents=[ch], metadatas=[{"source": meta_source}])
        total_chunks += len(chunks)
        print(f"[OK] Indexed {meta_source} -> {len(chunks)} chunks")

    print(f"[DONE] Indexed {len(docs)} docs, {total_chunks} chunks. DB at {CHROMA_DIR}/")

if __name__ == "__main__":
    main()