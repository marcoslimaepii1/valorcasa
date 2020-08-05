import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

localizacao = []
tamanho_quartos = []
valor = []
ratings =[]

url='https://imoveis.mercadolivre.com.br/casas/alagoas'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text())
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')

url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_49'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text())
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')

url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_97'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text())
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')

url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_145'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text())
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')

url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_193'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text()) 
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')


url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_241'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text()) 
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')


url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_289'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text()) 
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')



url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_337'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text()) 
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')




url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_385'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text()) 
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')




url='https://imoveis.mercadolivre.com.br/casas/alagoas_Desde_433'
try:
    html=urlopen(url)
    print('Pagina encontrada....')
    bs = BeautifulSoup(html,'lxml')
    casas = bs.select('.item__info-link')
    
    for casa in casas:
        localizacao.append(casa.find('div', class_='item__title').get_text())
        tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
        valor.append(casa.find('span', class_='price__fraction').get_text())     

        df = pd.DataFrame({
            "localizacao": localizacao,
            "tamanho_quartos": tamanho_quartos,
            "valor": valor,
        })
        df.head()
        df.to_csv('casas_alagoas.csv')
    
    
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found')





