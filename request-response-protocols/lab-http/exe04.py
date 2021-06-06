import requests

url = 'https://viacep.com.br/abc/'
cep = '30140071'
formato = '/xml/'

r = requests.get(url + cep + formato)

if r.status_code == 200:
    print('XML: ', r.text)
elif r.status_code == 404:
    print(r.status_code)
    print('Não houve sucesso na requisição')
    print(r.text)
