'''
mostrar na tela números pares entre 1 a 50
'''

print('NÚMEROS PARES')
d = int(input('Digite um número de 2 a 50: '))
print('Os números pares entre 1 e {} são: '.format(d))
for c in range(1, d+1):
    if c % 2 == 0:
        print(c)
