import requests

url = 'https://viacep.com.br/ws/'
uf = 'MG'
cidade = '/Belo Horizonte'
rua = '/Rua dos Aimores'
formato = '/json/'

r = requests.get(url + uf + cidade + rua + formato)

if r.status_code == 200:
    #print('XML: ', r.json())

    lista = r.json()

    print('Apenas o primeiro item: ', lista[0])
else:
    print('Ocorreu erro na requisição')

"""
import requests

r = requests.get('https://viacep.com.br/ws/' + '/MG' + '/Belo Horizonte' + '/Rua dos Aimorés' + '/json/')

if (r.status_code == 200):
    print('JSON : ', r.json())
    print()

    lista = r.json()

    print('Apenas o primeiro item: ', lista[0])

else:
    print('Nao houve sucesso na requisicao.')
"""