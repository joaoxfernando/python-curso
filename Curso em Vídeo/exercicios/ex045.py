from random import randint
from time import sleep

print('''VAMOS JOGAR JOKENPO? 
PEDRA = 1
PAPEL = 2
TESOURA 3''')
jogador = int(input('Qual sua jogada? '))
computador = int(randint(1,3))
itens = ('Pedra', 'Papel', 'Tesoura')

print('_'*21)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-='*10 +'-')
print('Você escolheu {}'.format(itens[jogador-1]))
print('Eu escolhi {}'.format(itens[computador-1]))
print('-='*10 + '-')

if jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
    print('\033[0;31;40mVOCÊ GANHOU!\033[0;0m')
elif jogador == 1 and computador == 2 or jogador == 2 and computador == 3 or jogador == 3 and computador == 1:
    print('\033[0;31;40mUhulll! Eu GANHEI! Seu noob!!!!\033[m')
elif jogador == 2 and computador == 2 or jogador == 1 and computador == 1 or jogador == 3 and computador == 3:
    print('\033[0;31;40mDeu empate.\033[m')
print('\nAdorei jogar com você, apareça mais vezes!')