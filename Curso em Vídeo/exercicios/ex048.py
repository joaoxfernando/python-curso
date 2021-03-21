'''
calcular a soma entre todos os números ímpares
que são múltiplos de 3 e que se encontram
no intervalo entre 1 a 500.
'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma = soma + c
print('A soma entre todos os {} valores solicitados é igual a {}'.format(cont, soma))