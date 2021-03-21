'''
desafio 009
mostrando a tabuada de um número que o usuário digitar
mas utilizando o laço FOR
'''

num = int(input('Digite um valor: '))
resultado = 0
print('-='*8+'-')
print('A tabuada do {} é:'.format(num))
for c in range(1, 11):
    resultado = num * c
    print('{} x {} = {}'.format(num, c, resultado))
print('-='*7+'-')