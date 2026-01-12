# FastAPI + Streamlit + LangChain RAG Chatbot

A complete **Retrieval-Augmented Generation (RAG)** chatbot built with **FastAPI (backend API)**, **Streamlit (frontend UI)**, **LangChain**, **FAISS**, and **Groq / LLM APIs**. This project allows you to upload PDFs, index them into a vector database, and chat with your documents.

---

## ✨ Features

* 📄 Upload and chat with **PDF documents**
* 🧠 **RAG pipeline** using LangChain
* 🔎 **FAISS** vector store for fast semantic search
* ⚡ **FastAPI** backend for document processing & QA
* 🎨 **Streamlit** frontend for interactive chat UI
* 🔐 Environment-based configuration using `.env`
* 🧩 Modular & beginner-friendly project structure

---

## 🏗️ Tech Stack

* **Backend**: FastAPI, Uvicorn
* **Frontend**: Streamlit
* **LLM**: Groq / OpenAI-compatible models
* **Embeddings**: HuggingFace Embeddings
* **Vector DB**: FAISS
* **RAG Framework**: LangChain
* **Language**: Python 3.10+

---

## 📁 Project Structure

```
fastapi-streamlit-rag-chatbot/
│
├── frontend.py
├── backend.py

```

---

## ⚙️ Installation

### 2️⃣ Install Dependencies



Or install separately for backend & frontend if needed.

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

---

## ▶️ Running the Project

### Start FastAPI Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

### Start Streamlit Frontend

```bash
cd frontend
streamlit run app.py
```

Frontend will run at:

```
http://localhost:8501
```

---

## 🔄 RAG Workflow (How It Works)

1. User uploads a PDF
2. PDF is loaded using `PyPDFLoader`
3. Text is split into chunks
4. Embeddings are generated
5. Chunks are stored in **FAISS**
6. User asks a question
7. Relevant chunks are retrieved
8. LLM generates an answer using retrieved context

---



If you have questions or want improvements, feel free to reach out.

Happy Building 🚀
