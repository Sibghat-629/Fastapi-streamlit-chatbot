import streamlit as st
import requests

st.set_page_config(page_title="PDF RAG Chatbot")
st.title("PDF Chatbot (FastAPI + RAG + Groq)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
    res = requests.post("http://127.0.0.1:8000/upload_pdf/", files=files)
    if res.status_code == 200:
        st.success(res.json()["message"])
    else:
        st.error("Failed to upload PDF")

question = st.text_input("Ask a question from PDF:")

if question:
    res = requests.get("http://127.0.0.1:8000/query/", params={"q": question})
    if res.status_code == 200 and "answer" in res.json():
        st.markdown(f"**Answer:** {res.json()['answer']}")
    else:
        st.error(res.json().get("error", "Upload PDF first"))
