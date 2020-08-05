import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    if request.args.get('key') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return request.key.get('key')
    # return jsonify({"message": "Não entre em pânico!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)