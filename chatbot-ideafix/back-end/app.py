from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_logic import process_message

app = Flask(__name__)
CORS(app)  # permite requisições do Angular

@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.get_json()
    pergunta = data.get('pergunta')
    resposta = process_message(pergunta)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
