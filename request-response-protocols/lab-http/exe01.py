import requests

"""
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/json/'

r = requests.get(url + cep + formato)

if(r.status_code == 200):
    print('JSON: ', r.json())
else:
    print('Requisição mal sucedida')
"""

url = 'https://viacep.com.br/ws/' #invocação a um web wervice
cep = '30140071'
formato = '/xml/'

r = requests.get(url + cep + formato)

if(r.status_code == 200):
    print('XML: ', r.text) #que retorna um XML
else:
    print('Requisição mal sucedida')