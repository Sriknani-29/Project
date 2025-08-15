from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


import os

# Load and process the PDF
pdf_path = "research_paper.pdf"
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    print(" Loading PDF document...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(" Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)

    print(f" Created {len(chunks)} chunks from PDF")

    # Convert chunks to documents with metadata
    processed_documents = []
    ids = []

    for i, chunk in enumerate(chunks):
        document = Document(
            page_content=chunk.page_content,
            metadata={
                "page": chunk.metadata.get("page", i),
                "source": pdf_path,
                "chunk_id": i
            },
            id=str(i)
        )
        ids.append(str(i))
        processed_documents.append(document)

vector_store = Chroma(
    collection_name="pdf_documents",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    print(" Adding documents to vector store...")
    vector_store.add_documents(documents=processed_documents, ids=ids)
    print(" Documents added to vector store!")
else:
    print(" Using existing vector store...")

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)