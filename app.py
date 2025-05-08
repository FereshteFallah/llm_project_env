from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)


model = pipeline('text-generation', model='gpt2')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    input_text = data.get('input_text', '')
    output = model(input_text, max_length=50, num_return_sequences=1)
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(debug=True,port=5000)
