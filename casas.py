import os
from flask import Flask, jsonify, request, render_template


app = Flask(__name__, template_folder='templates')

def preco(key1,key2):
    return 50000


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/calcula')
def testpoint():
    valor1 = request.args.get('key1')
    valor2 = request.args.get('key2')

    quartos = ''
    area = ''
    preco_estimado=preco(valor1, valor2)



    if valor1 =='1':
         quartos = '1 quarto'
    elif valor1 =='2':
         quartos = '2 quartos'
    elif valor1 =='3':
         quartos = '2 quartos'
    elif valor1 =='4':
         quartos = '4 quartos'
    elif valor1 =='5':
         quartos = '5 quartos'
    elif valor1 =='6':
         quartos = '6 ou mais quartos'
         

    if valor2 =='1':
         area = 'menor ou iual a 100 m2'
    elif valor2 =='2':
         area = 'maior que 100 m2 e menor ou iual a 200 m2'
    elif valor2 =='3':
         area = 'maior que 200 m2 e menor ou iual a 300 m2'
    elif valor2 =='4':
         area = 'maior que 300 m2 e menor ou iual a 400 m2'
    elif valor2 =='5':
         area = 'maior que 300 m2 e menor ou iual a 400 m2'
    elif valor2 =='6':
         area = 'maior que 500 m2 '
        
    
    return render_template('calculo.html', v1=quartos, v2=area, v3=preco_estimado)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)