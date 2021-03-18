'''
criar programa que leia um numero e mostre se é par ou ímpar

'''

num = int(input('Digite um número: '))

def éPar():
    if num % 2 == 0:
        print('O número {} é par!'.format(num))
    else:
        print('O número {} é ímpar!'.format(num))

éPar()