'''
aprimorar desafio anterior mostrando
a - a soma de todos os valores pares digitados
b - a soma dos valores da terceira coluna
c - o maior valor da 2ª linha
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição: {l,c}: '))
    if l > 0:
       maior = l
    elif l > maior:
        maior = l
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
for l in range(0, 3):
    somacol += matriz[l][2]
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da 2ª linha foi {maior}')
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma dos valores da 3ª coluna é: {somacol}')