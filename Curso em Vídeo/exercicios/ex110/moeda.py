def metade(preco=0, formato=False):
    metade = preco / 2
    return metade if formato is False else moeda(metade)


def dobro(preco=0, formato=False):
    dobro = preco * 2
    return dobro if formato is False else moeda(dobro)


def aumentar(preco=0, taxa=0, formato=False):
    aumentar = preco + (preco * taxa / 100)
    return aumentar if formato is False else moeda(aumentar)


def reduzir(preco=0, taxa=0, formato=False):
    reduzir = preco - (preco * taxa / 100)
    return reduzir if not formato else moeda(reduzir)


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco, aumento=10, desconto=13):
    # vAumento = preco * (1 + (aumento / 100))
    # vDesconto = preco * (1 - (desconto / 100))
    # dobro = preco * 2
    # metade = preco / 2
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado{":":>2} {moeda(preco):^14}')
    print(f'Dobro do preço{":":>3} {dobro(preco, True):^14}')
    print(f'Metade do preço{":":>2} {metade(preco, True):^14}')
    print(f'{aumento}% de aumento{":":>3} {aumentar(preco, aumento, True):^14}')
    print(f'{desconto}% de desconto{":":>2} {reduzir(preco, desconto, True):^14}')
    print('-' * 30)
