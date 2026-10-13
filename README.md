# 🔧 AD/AT Personal Codex

**Fully Local RAG Assistant for Analyst Developers & Analyst Testers**

------------------------------------------------------------------------

## 🎯 Overview

AD/AT Personal Codex is a **100% offline Retrieval-Augmented Generation
(RAG) assistant** designed specifically for:

-   Analyst Developers (AD)
-   Analyst Testers (AT)
-   DevOps & Release Teams

It runs entirely on your local machine using:

-   🧠 Ollama (Local LLM Inference)
-   🗄️ ChromaDB (Vector Database)
-   🔎 SentenceTransformers (Embeddings)
-   🌐 Streamlit (Chat UI)

No cloud APIs. No tracking. No data leaves your machine.

------------------------------------------------------------------------

## ✅ Features

  Feature                    Status
  -------------------------- --------
  Markdown & PDF ingestion   ✅
  Semantic Search (RAG)      ✅
  Local LLM Inference        ✅
  Structured Answers         ✅
  Chat-style UI              ✅
  CPU-only Mode              ✅

------------------------------------------------------------------------

## 📁 Project Structure

    ad-at-codex/
    ├── app.py
    ├── rag_index.py
    ├── rag_query.py
    ├── config.py
    ├── requirements.txt
    ├── .env
    ├── README.md
    ├── kb/
    ├── db/
    └── scripts/
        ├── bootstrap.bat
        └── run_app.bat

------------------------------------------------------------------------

## 🚀 Quick Start (Windows)

### Prerequisites

-   Windows 10/11
-   Python 3.11
-   8GB+ RAM recommended
-   Ollama installed

------------------------------------------------------------------------

### 1️⃣ Install Ollama

Download: https://ollama.com/download/windows

Verify installation:

    ollama --version

------------------------------------------------------------------------

### 2️⃣ Pull Model

    ollama pull phi3:3.8b
    ollama serve

------------------------------------------------------------------------

### 3️⃣ Setup Python Environment

    py -3.11 -m venv .venv
    .venv\Scripts\activate
    pip install --upgrade pip
    pip install -r requirements.txt

------------------------------------------------------------------------

### 4️⃣ Index Knowledge Base

    python rag_index.py

------------------------------------------------------------------------

### 5️⃣ Launch UI

    streamlit run app.py

Access: http://localhost:8501

------------------------------------------------------------------------

## 💬 Example Questions

-   How do I set up my dev environment?
-   What is our branching strategy?
-   Common build errors and fixes?
-   How to refresh test data?
-   CI/CD pipeline steps?
-   Release checklist?

------------------------------------------------------------------------

## ⚙️ Configuration (.env)

    OLLAMA_MODEL=phi3:3.8b
    TOP_K=4
    MAX_TOKENS_PER_CHUNK=450
    CHUNK_OVERLAP=80
    CHROMA_DIR=db
    KB_DIR=kb
    CHROMA_TELEMETRY_ENABLED=false
    ANONYMIZED_TELEMETRY=false

------------------------------------------------------------------------

## 🧠 Recommended Models

  Model         RAM     Speed          Quality
  ------------- ------- -------------- ------------
  phi3:3.8b     2.5GB   ⚡ Fast        ⭐⭐⭐⭐
  qwen2:1.5b    1.5GB   🚀 Very Fast   ⭐⭐⭐
  qwen2:7b      5GB+    🐌 Slow        ⭐⭐⭐⭐⭐
  llama3.2:3b   2GB     ⚡ Fast        ⭐⭐⭐⭐

------------------------------------------------------------------------

## 🔍 How It Works

    User Question
          ↓
    Embedding (SentenceTransformer)
          ↓
    ChromaDB Vector Search (Top-K)
          ↓
    Ollama Local LLM
          ↓
    Structured Answer in Streamlit UI

------------------------------------------------------------------------

## 🔒 Security & Privacy

-   Fully Offline
-   No Cloud APIs
-   No Data Tracking
-   Fully Auditable Source Code

------------------------------------------------------------------------

## 📊 Performance

  Operation          Time
  ------------------ -----------
  Index 10 Docs      \~30 sec
  Query Response     5--15 sec
  RAM Usage (phi3)   \~2.5GB

------------------------------------------------------------------------

## 📈 Future Improvements

-   PDF Table Extraction
-   OCR for Diagrams
-   Multi-Model Support
-   Export Answers to Markdown
-   VS Code Extension

------------------------------------------------------------------------

## 📄 License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a
copy...

------------------------------------------------------------------------

## 🙏 Acknowledgments

-   Ollama
-   ChromaDB
-   SentenceTransformers
-   Streamlit
-   BAAI/bge-small-en

------------------------------------------------------------------------

**⭐ Star this repository if it saves you time!**

*Last Updated: Feb 13, 2026*
