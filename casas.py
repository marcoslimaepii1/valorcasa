import os
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Teste  com index "})

@app.route('/teste')
def testpoint():
    valor = request.args.get('key1')
    
    return jsonify(valor)
    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)