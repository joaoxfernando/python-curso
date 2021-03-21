'''
ler um numero e mostrar seu fatorial
ex: 5! = 5x4x3x2x1=120
'''
from math import factorial

print('CALCULANDO FATORIAL...')

fator = int(input('Digite  um número para calcular o seu fatorial: '))
f = 1
n = fator
print('{}! = '.format(fator), end='')
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= f
    n -= 1
print(f)