from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector_rag import retriever

model = OllamaLLM(model="gemma:2b")

template = """
You are an expert in analyzing research papers and academic documents.

Here are some relevant sections from the research paper: {context}

Here is the question to answer: {question}

Please provide a comprehensive answer based on the information from the research paper. If the information is not available in the provided context, please say so.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

print(" PDF Research Paper Q&A System")
def new_func():
    print("=" * 40)
    print("Ask questions about the research paper content.")
    print("Type 'q' to quit.")
    print()

new_func()

while True:
    print("\n" + "-" * 40)
    question = input("Ask your question (q to quit): ")
    print()

    if question.lower() == "q":
        print(" Goodbye!")
        break

    if question.strip():
        try:
            # Retrieve relevant sections from the PDF
            relevant_docs = retriever.invoke(question)

            # Combine the relevant sections into context
            context = "\n\n".join([doc.page_content for doc in relevant_docs])

            # Generate answer using the LLM
            result = chain.invoke({"context": context, "question": question})
            print(" Answer:", result)

        except Exception as e:
            print(f" Error: {e}")
            print("Please make sure Ollama is running and the model is available.")