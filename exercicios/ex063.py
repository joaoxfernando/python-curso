'''
ler número inteiro
e mostre na tela os 'n' primeiro termos de uma sequencia de fibonacci
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('-'*25)
print(' Sequência de Fibonacci')
print('-'*25)

num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*25)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    cont += 1
print(' → Acabou...')
print('~'*25)