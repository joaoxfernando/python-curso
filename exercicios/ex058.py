'''
melhorar desafio 28
onde comp pensa num numero de 0 a 10
agora o jogador vai ficar tentando até acertar
mostrando no final quantas vezes foram necessárias ate o acerto
'''

from random import randint
cpu = int(randint(1, 100))
acertou = False
jogador = -1
cont = 0

print('='*22)
print('JOGO DA ADIVINHAÇÃO')
print('='*22)
print('''Acabei de pensar em um número...
Você consegue adivinhar qual número eu pensei?''')

while not acertou:
    jogador = int(input('Tente acertar o número (de 1 a 100): '))
    cont += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('Mais... tente novamente.')
        elif jogador > cpu:
            print('Menos... tente novamente.')
print('Você acertou, eu realmente escolhi o número {}'.format(cpu))
if cont > 1:
    print('Precisou de {} tentativas para acertar.'.format(cont))
else:
    print('VOCÊ É O CARA! ACERTOU DE PRIMEIRA!!!')
