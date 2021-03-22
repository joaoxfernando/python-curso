def contador(i, f, p):
    """
    >> Faz uma contagem e mostra na tela.
    :param i: Ínicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """

    """"""
    c = i
    while i <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


help(contador)


