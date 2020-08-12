import os
from flask import Flask, jsonify, request, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/calcula')
def testpoint():
    valor1 = request.args.get('key1')
    valor2 = request.args.get('key2')

    return render_template('calculo.html')
    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)