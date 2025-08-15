# Research Paper Q&A System

## Overview
The **Research Paper Q&A System** is a Flask-based web application that allows users to:
- Upload a research paper in PDF format.
- Automatically extract and store the document’s content using **LangChain** and **ChromaDB**.
- Ask natural language questions about the research paper and get accurate answers.
- Use **Ollama** for local embeddings and language model responses.

This project demonstrates **RAG (Retrieval-Augmented Generation)** to retrieve relevant document chunks and generate AI-based answers.

---

## Features
- **Upload PDFs** directly from the browser.
- **Text Chunking** using `RecursiveCharacterTextSplitter`.
- **Vector Store** with `ChromaDB` for fast retrieval.
- **Semantic Search** for context-based answers.
- **LLM-powered responses** using `Ollama`.
- **Flask Web Interface** for easy interaction.

---

## Tech Stack
- **Backend:** Python, Flask  
- **LLM & Embeddings:** LangChain, Ollama (`mxbai-embed-large`)  
- **Vector Database:** ChromaDB  
- **Document Loader:** PyPDFLoader  
- **Frontend:** HTML, CSS, JavaScript  

---

## Project Structure
Project/
│── app.py # Flask application entry point
│── vector.py # Vector store creation and PDF processing
│── vector_rag.py # RAG implementation for queries
│── main_rag.py # CLI version for testing Q&A
│── templates/
│ └── index.html # Frontend interface
│── static/ # CSS, JS, images
│── research_paper.pdf # Sample research paper
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---

## How to Run Locally

### 1️ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/PROJECT_NAME.git
cd PROJECT_NAME

