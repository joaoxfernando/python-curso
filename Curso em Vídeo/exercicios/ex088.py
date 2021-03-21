'''
programa para criar palpites da mega sena
vai perguntar qnts jogos serão gerados
programa vai sortear 6 numeros de 1 a 60 para cada jogo
cadastrando tudo em uma lista composta
'''

from random import randint
from time import sleep
print('-'*30)
print(f'JOGO DA MEGA SENA'.center(30))
print('-'*30)
lista = list()
jogos = list()
quant = int(input('Quantos jogos deseja sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

if quant == 1:
    print('=' * 4, f' SORTEANDO JOGO ÚNICO ', '=' * 4)
else:
    print('=' * 5, f' SORTEANDO {quant} JOGOS ', '=' * 5)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=' * 7, ' * BOA SORTE! * ', '=' * 7)