import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

localizacao = []
tamanho_quartos = []
valor = []
ratings =[]

pagecount=1


while pagecount < 41:
    
    if pagecount == 1:
        url='https://imoveis.mercadolivre.com.br/casas'
        try:
            html=urlopen(url)
            print('Pagina encontrada....', url)
            bs = BeautifulSoup(html,'lxml')
            casas = bs.select('.item__info-link')
            
            for casa in casas:
                localizacao.append(casa.find('div', class_='item__title').get_text())
                tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
                valor.append(casa.find('span', class_='price__fraction').get_text())
            
            
        except HTTPError as e:
            print(e)
        except URLError as e:
            print('The server could not be found', url)
    elif pagecount < 40:
        url='https://imoveis.mercadolivre.com.br/casas_Desde_'+str(((pagecount-1)*48)+1)
        try:
            html=urlopen(url)
            print('Pagina encontrada....', url)
            bs = BeautifulSoup(html,'lxml')
            casas = bs.select('.item__info-link')
            
            for casa in casas:
                localizacao.append(casa.find('div', class_='item__title').get_text())
                tamanho_quartos.append(casa.find('div', class_='item__attrs').get_text())
                valor.append(casa.find('span', class_='price__fraction').get_text())
            
            
        except HTTPError as e:
            print(e)
        except URLError as e:
            print('The server could not be found', url)
    else:
        url='https://imoveis.mercadolivre.com.br/casas_Desde_'+str((pagecount-1)*48)
        try:
            html=urlopen(url)
            print('Pagina encontrada....', url)
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
                df.to_csv('casas.csv')
        except HTTPError as e:
            print(e)

        except URLError as e:
            print('The server could not be found', url)

    pagecount = pagecount+1



