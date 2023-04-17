import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    # Get the input text from the request
    input_text = request.get_json()['input_text']
    API_URL = "https://api-inference.huggingface.co/models/nomic-ai/gpt4all-j"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": str(input_text),
        "options":{
        "wait_for_model":True
        }
    })
    return json.dumps(output[0]['generated_text'])

if __name__ == '__main__':
    app.run(debug=True)