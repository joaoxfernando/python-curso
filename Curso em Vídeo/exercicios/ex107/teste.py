from ex108 import moeda

preco = int(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(preco)} é igual a R$ {moeda.metade(preco):.2f}')
print(f'O dobro de R$ {moeda.moeda(preco)} é igual a R$ {moeda.dobro(preco):.2f}')
print(f'O valor de R$ {moeda.moeda(preco)} acrescido 10% é igual a R$ {moeda.aumentar(preco, 10):.2f}')
print(f'O valor de R$ {moeda.moeda(preco)} com 13% de desconto é igual a R$ {moeda.reduzir(preco, 13)}')