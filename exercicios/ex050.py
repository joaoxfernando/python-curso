'''
ler seis números inteiros
e mostre a soma apenas dos números pares
se for impar desconsiderar.
'''

soma = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print('A soma entre todos os números pares digitados é igual a: {}'.format(soma))