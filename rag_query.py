import subprocess
import shutil
import chromadb
from sentence_transformers import SentenceTransformer
from config import OLLAMA_MODEL, CHROMA_DIR, TOP_K


def _ollama_available() -> bool:
    """Check if the 'ollama' CLI is available on PATH."""
    return shutil.which("ollama") is not None


def call_ollama(prompt: str, model: str = OLLAMA_MODEL) -> str:
    """Call Ollama via CLI with the given prompt."""
    if not _ollama_available():
        return "[ERROR] Ollama not found. Please install Ollama, add it to PATH, and ensure it is running."

    try:
        proc = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=180
        )
        if proc.returncode != 0:
            return f"[LLM ERROR] {proc.stderr.decode('utf-8', errors='ignore')}"
        return proc.stdout.decode("utf-8", errors="ignore")
    except subprocess.TimeoutExpired:
        return "[ERROR] Ollama call timed out. Try a smaller model or shorter prompt."


def retrieve_and_answer(question: str) -> str:
    """Retrieve context from Chroma and get a structured answer from Ollama."""
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    col = client.get_or_create_collection("codex")

    embedder = SentenceTransformer("BAAI/bge-small-en")
    q_emb = embedder.encode(question).tolist()

    res = col.query(query_embeddings=[q_emb], n_results=TOP_K)
    docs = res.get("documents", [[]])[0]
    metas = res.get("metadatas", [[]])[0]

    if not docs:
        ctx = "NO_CONTEXT"
        sources_str = "None"
    else:
        context_blocks = []
        sources = []
        for d, m in zip(docs, metas):
            src = m.get("source", "unknown")
            context_blocks.append(f"Source: {src}\n{d}")
            sources.append(src)
        ctx = "\n\n".join(context_blocks)
        sources_str = ", ".join(sorted(set(sources)))

    prompt = f"""
You are AD/AT Codex, an assistant for Analyst Developers and Analyst Testers.
Answer ONLY using the provided context. If the context is NO_CONTEXT, say you have no information.

Context:
{ctx}

Question: {question}

Respond in this exact structure:

Summary:
- [1–3 bullet points summarizing the answer]

Steps:
1. [step 1]
2. [step 2]
3. [step 3]

Notes:
- [important notes, pitfalls, assumptions]

Sources:
- {sources_str}
"""

    return call_ollama(prompt)


if __name__ == "__main__":
    print(retrieve_and_answer("How do I set up the local environments?"))
