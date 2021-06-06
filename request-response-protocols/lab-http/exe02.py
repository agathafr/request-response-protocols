import requests
import time

url = 'https://viacep.com.br/ws/'
lista_ceps = ['30140071', '30140072', '30140073', '30140074', '30140075', '30140076']
formato = '/xml/'

for x in lista_ceps: #variável x pega cada um dos ceps de lista_ceps
    r = requests.get(url + x + formato) #e monta a url para fazer a requisição

    if r.status_code == 200:
        print('CEP:', x) #imprime o cep
        print('XML:', r.text) #mostra o que o servidor retornou
    else:
        print('Erro na requisição')

    time.sleep(2.4) #mostra o resultado a cada 2.4 segundos
