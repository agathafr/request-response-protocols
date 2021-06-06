import requests

r = requests.get('http://www.google.com/search', params={'q': 'agatha christie'})

if r.status_code == 200:
    print('Retorno:', r.text)

    arq = open('c:\\temp\\d_google.html', 'w')

    arq.write(r.text)

    arq.close()
else:
    print('Erro na requisição', r.status_code)