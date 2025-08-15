import os
import shutil
import gc
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
os.environ["OLLAMA_NO_GPU"] = "1"



# Path to the research paper PDF
pdf_path = "research_paper.pdf"

# Location to store the Chroma DB
db_location = "./chrome_langchain_db"

# Embedding model
embedding = OllamaEmbeddings(model="mxbai-embed-large")




# Function to add a PDF to the vector store and update retriever
def add_pdf_to_vectorstore(path):
    global retriever

    if not os.path.exists(path):
        raise FileNotFoundError(f"PDF not found: {path}")

    # Remove old DB before creating a new one
    try:
        if os.path.exists(db_location):
            shutil.rmtree(db_location, ignore_errors=True)
    except Exception as e:
        print(f"Warning: Could not remove old DB: {e}")

    gc.collect()

    # Load and split the PDF
    loader = PyPDFLoader(path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)

    # Create new Chroma DB
    db = Chroma.from_documents(chunks, embedding, persist_directory=db_location)

    # Update retriever
    retriever = db.as_retriever()
    return retriever
    print(f"Vector store rebuilt from: {path}")

# Global retriever so it can be updated after uploads
retriever = add_pdf_to_vectorstore(pdf_path)

# Build the vector store at startup if the PDF exists
if os.path.exists(pdf_path):
    add_pdf_to_vectorstore(pdf_path)
else:
    print(f"No initial PDF found at {pdf_path}. Upload one via /upload to begin.")
