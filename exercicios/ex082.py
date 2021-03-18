'''
ler vários numeros e add na lista
criar duas listas extras que vão contar os valores pares e impares separadamente
ao final mostre as tres listas.
'''

lista = []
pares = []
impares = []
continuar = 'S'

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N')).upper()[0]
    if continuar == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Os valores digitados foram: {lista}')
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares são: {impares}')