'''
ler peso de 5 pessoas
mostrar maior e menor peso
'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.2f} kgs'.format(maior))
print('O menor peso lido foi de {:.2f} kgs'.format(menor))