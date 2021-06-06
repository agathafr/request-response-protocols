import requests

# Leitura de um campo do canal(temperatura e umidade) em JSON - Requisição de visualização de dados
r = requests.get('https://api.thingspeak.com/channels/1226973/fields/1.json?api_key=RTLY3MGRNANNANTQ&results=2')

# Atualização - Requisição de envio de dados
# r = requests.get('https://api.thingspeak.com/update?api_key=X7AASPFZ94RV1CK1&field2=81')

print('Código de status: ', r.status_code)

if (r.status_code == 200):
    print(r.text)
