# Linha ajustável ao tamanho da frase...
def escreva(txt):
    linha = len(txt) + 4
    print('-' * linha)
    print(f'{txt:^{linha}}')
    print('-' * linha)

while True:
    frase = str(input('Digite uma frase qualquer: '))
    escreva(frase)
    continuar = str(input(f'{"Quer digitar outra frase? [S/N]"}\n')).upper()
    if continuar[0] == 'N':
        print('ENCERRANDO...')
        break
