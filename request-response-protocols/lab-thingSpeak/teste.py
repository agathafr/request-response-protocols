from random import randint
import time
temperatura = [randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40), randint(10,40)]
umidade = [randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80), randint(50,80)]


for grau in temperatura:
    print(grau)
    time.sleep(1.0)

print(" ")

for percent in umidade:
    print(percent)
    time.sleep(1.0)