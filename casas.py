import os
from flask import Flask, jsonify, request
from app import app


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', title='Home')

@app.route('/teste')
def testpoint():
    valor = request.args.get('key1')
    
    return jsonify(valor)
    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)