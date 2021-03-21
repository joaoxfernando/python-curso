'''
ler numero inteiro
mostrar se ele é ou não um número primo.
'''

print('='*30)
print('   VERIFICAR DE NÚMERO PRIMO')
print('='*30)
num = int(input('Digite um número: '))
contprimo = 0
cont = 0
for c in range(1, num+1):
    # print('{} '.format(c), end='')
    if num % c == 0:
        print('\033[0;33;40m{}\033[m'.format(c), end=' ')
        contprimo += 1
    else:
        cont += 1
        print('\033[0;31;40m{}\033[m'.format(c), end=' ')

if contprimo == 2:
    print('\nO número {} É PRIMO!'.format(num))
else:
    print('\nO número {} NÃO É PRIMO!'.format(num))