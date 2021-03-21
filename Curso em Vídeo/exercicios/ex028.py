'''fazer computador 'pensar' num número de 0 a 5
e fazer usuário tentar descobrir o número pensado
escrever se acertou ou não
'''

from random import randint

print('VOU PENSAR EM UM NÚMERO ENTRE 0 e 5. TENTE ADIVINHAR..')

def jogar():
    num = int(input('Qual número você acha que estou pensando? '))
    numPC = randint(0, 5)
    if num == numPC:
        print('VOCÊ ACERTOU! Eu pensei no número {}'.format(numPC))
    else:
        print("GAME OVER! Você pensou no número {} e eu pensei no {}".format(num, numPC))
jogar()

playAgain = int(input("Tecla 1 caso queira jogar novamente!"))

if playAgain == 1:
    jogar()
else:
    print('\033[0;30;41mObrigado por jogar comigo!\033[m')
