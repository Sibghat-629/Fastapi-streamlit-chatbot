from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
import tempfile
from pydantic import SecretStr

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains.qa_with_sources.retrieval import RetrievalQA  # v1.2.3
from langchain_groq import ChatGroq

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔴 HARDCODED GROQ API KEY
GROQ_API_KEY = SecretStr("gsk_REPLACE_WITH_YOURS")

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    api_key=GROQ_API_KEY
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = None

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    global vectorstore

    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(await file.read())
    tmp.close()

    reader = PdfReader(tmp.name)
    text = "".join(page.extract_text() or "" for page in reader.pages)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    docs = splitter.create_documents([text])

    vectorstore = FAISS.from_documents(docs, embeddings)

    return {"status": "PDF loaded successfully"}

@app.get("/query/")
async def query(q: str):
    if vectorstore is None:
        return {"error": "Upload a PDF first"}

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return {"answer": qa.run(q)}
