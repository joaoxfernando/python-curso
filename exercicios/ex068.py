'''
jogar par ou impar com o computador
só interrompe quando o jogador perder
mostrando o total de vitórias consectivas que ele conquistou
'''

from random import randint

numjogador = comp = soma = 0
cont = 0
while True:
    jogador = int(input('Jogue um número de 0 a 5: '))
    escolhajogador = ' '
    while escolhajogador not in 'PI':
        escolhajogador = str(input('Você quer par ou ímpar? [P/I]: ')).upper()[0]
    print('~'*27)
    comp = int(randint(0, 5))
    soma = jogador + comp
    if soma % 2 == 0 and escolhajogador == 'P':
        print(f'Você ganhou, pois {soma} é par.')
        print('~' * 27)
    elif soma % 2 != 0 and escolhajogador == 'I':
        print(f'Você ganhou, pois {soma} é ímpar.')
        print('~' * 27)
    elif soma % 2 != 0 and escolhajogador == 'P':
        print(f'Você perdeu, pois {soma} é ímpar.', end='')
        break
    elif soma % 2 == 0 and escolhajogador == 'I':
        print(f'Você perdeu, pois {soma} é par.', end='')
        break
    cont += 1
if cont < 1:
    print(f' Você não me venceu nenhuma vez. HAHAH PERDEDOR!')
    print('~' * 27)
elif cont == 1:
    print(f' Você só me venceu {cont} vez... tsc tsc')
    print('~' * 27)
elif 2 <= cont < 5:
    print(f' Após {cont} vitórias seguidas..')
    print('~' * 27)
elif cont >= 5:
    print(f' FINALMENTE! Você já tinha me vencido {cont} vezes seguidas.')
    print('~' * 27)
elif cont >= 10:
    print(f' QUE TIPO DE DEUS É VOCÊ? ME VENCEU {cont} fucking vezes seguidas.')
    print('~' * 27)