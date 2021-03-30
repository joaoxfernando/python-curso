def metade(preco=0):
    metade = preco / 2
    return metade


def dobro(preco=0):
    dobro = preco * 2
    return dobro


def aumentar(preco=0, taxa=0):
    aumentar = preco + (preco * taxa / 100)
    return aumentar


def reduzir(preco=0, taxa=0):
    reduzir = preco - (preco * taxa / 100)
    return reduzir


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco, aumento, desconto):
    vAumento = preco * (1 + (aumento / 100))
    vDesconto = preco * (1 - (desconto / 100))
    dobro = preco * 2
    metade = preco / 2
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado{":":>2} {preco:^18.2f}')
    print(f'Dobro do preço{":":>3} {dobro:^18.2f}')
    print(f'Metade do preço{":":>2} {metade:^18.2f}')
    print(f'{aumento}% de aumento{":":>3} {vAumento:^18.2f}')
    print(f'{desconto}% de desconto{":":>2} {vDesconto:^18.2f}')
    print('-' * 30)
