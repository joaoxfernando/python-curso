'''
gerar 5 números aleatórios e colocar em uma tupla
depois disso mostrar a listagem de numeros gerados
mostrar menor e maior numero
'''
from random import randint

lista = tuple(randint(i + 1, 9) for i in range(0, 5))
maior = menor = cont = 0
print(f'Os números sorteados foram: ', end='')
for num in lista:
    cont += 1
    print(f'{num}', end=' ')
    if cont == 1:
        menor = maior = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'\nO menor número foi: {menor} e o maior: {maior}')