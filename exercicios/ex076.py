'''
tupla unica com nome de produtos e preços
organizar produtos de forma tabular
'''

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Caneta', 3.50,
            'Estojo', 5.00,
            'Mochila', 55.00,
            'Livro', 39.90)
print('-'*33)
print(f'{"LISTAGEM DE PREÇOS":^31}')
print('-'*33)
for l in range(0, len(listagem)):
    if l % 2 == 0:
        print(f'{listagem[l]:.<25}', end='')
    else:
        print(f'R${listagem[l]:>6.2f}')