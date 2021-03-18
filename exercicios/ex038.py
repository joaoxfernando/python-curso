'''
ler e comparar dois numeros inteiros para saber quem é menor e quem é menor
'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O primeiro número escolhido: {} é maior que o segundo: {}'.format(n1, n2))
elif n1 == n2:
    print('Os dois números são iguais.')
else:
    print('O segundo número escolhido: {} é maior que o primeiro: {}'.format(n2, n1))