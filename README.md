
```markdown
#  Research Paper Q&A System

##  Overview
The **Research Paper Q&A System** is a Flask-based web application that allows users to:
- Upload a research paper in PDF format.
- Automatically extract and store the document’s content using **LangChain** and **ChromaDB**.
- Ask natural language questions about the research paper and get accurate answers.
- Use **Ollama** for local embeddings and language model responses.

This project demonstrates **RAG (Retrieval-Augmented Generation)** to retrieve relevant document chunks and generate AI-based answers.

---

##  Features
-  **Upload PDFs** directly from the browser.
-  **Text Chunking** using `RecursiveCharacterTextSplitter`.
-  **Vector Store** with `ChromaDB` for fast retrieval.
-  **Semantic Search** for context-based answers.
-  **LLM-powered responses** using `Ollama`.
-  **Flask Web Interface** for easy interaction.

---

##  Tech Stack
- **Backend:** Python, Flask  
- **LLM & Embeddings:** LangChain, Ollama (`mxbai-embed-large`)  
- **Vector Database:** ChromaDB  
- **Document Loader:** PyPDFLoader  
- **Frontend:** HTML, CSS, JavaScript  

---

##  Project Structure
```

Project/
│── app.py                # Flask application entry point
│── vector.py              # Vector store creation and PDF processing
│── vector\_rag.py          # RAG implementation for queries
│── main\_rag.py            # CLI version for testing Q\&A
│── templates/
│   └── index.html         # Frontend interface
│── static/                # CSS, JS, images
│── research\_paper.pdf     # Sample research paper
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation

````

---

##  How to Run Locally

### 1️ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/PROJECT_NAME.git
cd PROJECT_NAME
````

### 2️ Create & Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️ Install and Run Ollama

Download Ollama from: [https://ollama.ai](https://ollama.ai)
Then pull the embedding model:

```bash
ollama pull mxbai-embed-large
```

### 5️ Start Flask App

```bash
python app.py
```

Access the app in your browser at:

```
http://127.0.0.1:5000
```

---

##  How It Works

1. **Upload PDF** → The PDF is split into chunks.
2. **Embedding** → Each chunk is converted into embeddings using `OllamaEmbeddings`.
3. **Vector Storage** → Embeddings are stored in `ChromaDB`.
4. **Query** → User asks a question.
5. **Retriever** → System searches for relevant chunks.
6. **Answer Generation** → LLM generates a response based on retrieved chunks.


Screenshot

---

##  Author

Developed by **\[SRIKANTH AMUDALA VEERARAGHAVALU]**

---

##  License

This project is licensed under the MIT License.

```


