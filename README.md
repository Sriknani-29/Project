# Retrieval-Augmented Generation (RAG) System for Academic Research Papers using LLMs

## Overview 
This project is a **Retrieval-Augmented Generation (RAG)** system that allows users to upload academic research papers (PDFs) and ask natural language questions to extract context-aware answers.

It uses **Large Language Models (LLMs), vector databases, and semantic search** to go beyond traditional keyword-based document retrieval.

The system is built using **Flask, LangChain, ChromaDB, and Ollama**, enabling efficient document understanding and AI-powered question answering.

---

## Problem Statement
Traditional document search systems rely on keyword matching, which fails to understand context and semantic meaning.

This project solves that problem by:
- Converting documents into vector embeddings  
- Storing them in a vector database  
- Retrieving semantically relevant content  
- Generating accurate responses using an LLM  
---

## Features
- Upload PDF research papers via web interface  
- Automatic text extraction and chunking  
- Vector embeddings stored in ChromaDB  
- Semantic search across document content  
- Context-aware question answering using LLMs  
- Simple Flask-based web interface  

---

## Tech Stack
- **Backend:** Python, Flask  
- **LLM & Embeddings:** LangChain, Ollama (mxbai-embed-large)  
- **Vector Database:** ChromaDB  
- **Document Processing:** PyPDFLoader, RecursiveCharacterTextSplitter  
- **Frontend:** HTML, CSS, JavaScript  

---

## How It Works (Architecture)

1. User uploads a PDF document  
2. The document is split into smaller chunks  
3. Each chunk is converted into embeddings  
4. Embeddings are stored in ChromaDB  
5. User submits a query  
6. Query is converted into vector form  
7. Relevant document chunks are retrieved  
8. LLM generates a final contextual response  

## Project Structure
```bash
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
```

---
## How to Run Locally

### 1️ Clone the Repository

git clone https://github.com/YOUR_USERNAME/PROJECT_NAME.git

---

## Create and Activate Virtual Environment

bash 
python -m venv venv

# Windows
venv\Scripts\activate

---

##Install and Run Ollama

# Download Ollama from: https://ollama.ai
Then pull the embedding model:

ollama pull mxbai-embed-large

---

## Start Flask App By Running
python app.py

---

##Access the application in browser at:
http://127.0.0.1:5000

---


