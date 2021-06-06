import requests
from random import randint
import time

temperatura = [randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40), randint(15,40)]
umidade = [randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80)]

for grau in temperatura:
    r = requests.get('https://api.thingspeak.com/update?api_key=57ESTMYU4CWZGRSQ&field1=' + str(grau))
    time.sleep(60.4)

for porcent in umidade:
    r = requests.get('https://api.thingspeak.com/update?api_key=57ESTMYU4CWZGRSQ&field2=' + str(porcent))
    time.sleep(60.4)
