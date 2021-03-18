'''
cadastrar nome e preco de varios produtos
perguntar se deseja continuar
no final mostrar:
a - total gasto
b - quantos produtos custam mais de 1000
c - qual nome do mais barato.
'''
nomebarato = produto = ''
cont = preco = barato = total = maisdemil = 0
continuar = 'S'

while continuar in 'Ss':
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    cont += 1
    if cont == 1:
        menor = preco
        nomebarato = produto
    if preco > 1000:
        maisdemil += 1
    elif preco :
        barato = preco
        nomebarato = produto
    continuar = str('Deseja continuar cadastrando produtos? [S/N]').upper().strip()[0]
    if continuar == 'Nn':
        break
print(f'O total gasto foi de: R${total}')
print(f'{maisdemil} produtos custam mais de R$1000,00.')
print(f'O produto mais barato foi a {nomebarato} e custa {barato}')