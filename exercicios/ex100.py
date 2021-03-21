'''
uma lista chamada numeros e duas funções chamada sorteia e somaPar
a primeira vai sortear 5 numeros e coloca-los dentro da lista e a segunda vai
mostrar a soma entre todos os valores PARES sorteados da funçao anterior
'''
from random import randint
numeros = list()
par = list()
def sorteia(numeros):
    print('SORTEANDO 5 VALORES...', end='')
    for i in range(0, 5):
        n = randint(0, 50)
        numeros.append(n)
        print(f'{n} ', end='')

def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
            par.append(n)
    print(f'\nA soma dos numeros {par} é igual a {soma}.')


sorteia(numeros)
somaPar()
