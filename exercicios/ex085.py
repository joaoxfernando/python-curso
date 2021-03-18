'''
sete valores e cadastre numa unica listsa
separar numeros pares e impares.
no final mostrar valores pares e impares em ordem crescente
'''

lista = [[], []]
for c in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()
print('='*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')