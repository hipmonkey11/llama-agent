import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2:7b")
TOP_K = int(os.getenv("TOP_K", "4"))
CHROMA_DIR = os.getenv("CHROMA_DIR", "db")
KB_DIR = os.getenv("KB_DIR", "kb")
MAX_TOKENS_PER_CHUNK = int(os.getenv("MAX_TOKENS_PER_CHUNK", "450"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "80"))