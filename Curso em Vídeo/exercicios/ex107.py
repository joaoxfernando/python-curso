import moeda

preco = int(input('Digite o preço: R$ '))
print(f'A metade de R$ {preco} é igual a R$ {moeda.metade(preco):.2f}')
print(f'O dobro de R$ {preco} é igual a R$ {moeda.dobro(preco):.2f}')
print(f'O valor de R$ {preco} acrescido 10% é igual a R$ {moeda.aumentar10(preco):.2f}')
print(f'O valor de R$ {preco} com 13% de desconto é igual a R$ {moeda.reduzir13(preco)}')