'''
função contador que receba tres parametros:
inicio, fim, passo e realize a contagem.
programa terá que realizar tres contagens atraves da função criada
a - de 1 até 10 de 1 em 1
b - de 10 a 0 de 2 em 2
c - uma contagem personalizada
'''
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} contando de {p} em {p}')
    sleep(2.2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.7)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
        print('FIM!')

# contador(1, 10, 1)
# contador(10, 0, 2)

while True:
    inicio = input('Início: ')
    if not inicio.isnumeric():
        print('Digite um valor numérico.')
    else:
        break
while True:
    fim = input('Fim: ')
    if not fim.isnumeric():
        print('Digite um valor numérico.')
    else:
        break
try:
    passo = int(input('Passo: '))
except ValueError:
    print('Digite um valor numérico.')

contador(int(inicio), int(fim), passo)
