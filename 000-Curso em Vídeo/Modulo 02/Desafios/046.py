"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.

"""

import os
from time import sleep

os.system('cls')

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('FIM, ...')