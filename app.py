from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from converter import text_to_ogg
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": '*'}})  # Enable Cross-Origin Resource Sharing

# Initialize LangChain with Ollama
ollama_llm = Ollama(model="llama3.1:latest")  # Replace with your Ollama model
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question: {question}"
)
llama_chain = LLMChain(llm=ollama_llm, prompt=prompt_template)

# Define a function to process the question
def get_ollama_response(question):
    return llama_chain.run(question)

@app.route('/api/process', methods=['POST' , 'GET'])
def process_question():
    print("Request Received")
    # if request.method == 'POST':    
    data = request.get_json()  # Get the JSON data from the request
    user_question = data.get('question')

    if not user_question:
        return jsonify({"error": "No question provided"}), 400
        #return jsonify({"response": "Hello I am under water"}), 200

    # Get response from Ollama via LangChain
    try:
        processed_response = get_ollama_response(user_question)
        text_to_ogg(dialogue_file_name='res_text.txt',text=processed_response, output_filename='response.ogg', output_filename_mp3='response.mp3')
        print(processed_response)

    

    except Exception as e:
            return jsonify({"error": str(e)}), 500


    return jsonify({"response": processed_response}), 200


if __name__ == '__main__':
    app.run(debug=True)
