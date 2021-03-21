'''
função chamada maior() que recebe vários números:
programa tem que ler todos e dizer qual maior!
'''
from time import sleep

def maior(* num):
    print('-' * 30)
    cont = maior = 0
    print('Checando os valores informados...')
    print('Os valores informados foram: ', end='')
    for n in num:
        print(f'{n} ', end='')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'\nForam informado ao todo {cont} números.')
    sleep(0.4)
    print(f'E o maior valor informado foi: {maior}.')

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite o último número: '))

maior(a, b, c)
