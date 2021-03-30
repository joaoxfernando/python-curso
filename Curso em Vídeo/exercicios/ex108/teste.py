import moeda

preco = int(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(preco)} é igual a R$ {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de R$ {moeda.moeda(preco)} é igual a R$ {moeda.moeda(moeda.dobro(preco))}')
print(f'O valor de R$ {moeda.moeda(preco)} acrescido 10% é igual a R$ {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'O valor de R$ {moeda.moeda(preco)} com 13% de desconto é igual a R$ {moeda.moeda(moeda.reduzir(preco, 13))}')