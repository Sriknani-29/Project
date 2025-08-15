from flask import Flask, render_template, request, jsonify
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever, add_pdf_to_vectorstore
import os


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Initialize the model and prompt chain
model = OllamaLLM(model="phi:2.7b")

template = """
You are an expert in analyzing research papers and academic documents.

Here are some relevant sections from the research paper: {context}

Here is the question to answer: {question}

Please provide a comprehensive answer based on the information from the research paper.
If the information is not available in the provided context, please say so.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        question = data.get('question', '').strip()

        if not question:
            return jsonify({'error': 'Question cannot be empty'}), 400

        relevant_docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])
        result = chain.invoke({"context": context, "question": question})

        return jsonify({
            'answer': str(result),
            'question': question
        })

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            # Always overwrite research_paper.pdf so vector.py uses the latest file
            filepath = "research_paper.pdf"
            file.save(filepath)

            # Rebuild the vector store from the new PDF
            add_pdf_to_vectorstore(filepath)

            return jsonify({'message': 'File uploaded and processed successfully'}), 200

        except Exception as e:
            return jsonify({'error': f'Processing failed: {str(e)}'}), 500

    return jsonify({'error': 'Invalid file type'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
