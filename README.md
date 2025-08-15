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
