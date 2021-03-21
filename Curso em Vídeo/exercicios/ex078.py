'''
ler 5 numeros e guardar numa lista

no final mostre qual foi o maior e qual foi o menor e suas posições
'''

lista = []

for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
c = maior = menor = posmenor = posmaior = 0
for l in lista:
    if c == 0:
        maior = l
        menor = l
    else:
        if l > maior:
            maior = l
            posmaior = c
        elif l < menor:
            menor = l
            posmenor = c
    c += 1
print(f'O menor valor foi o {menor} encontrado na posição {posmenor}')
print(f'O maior valor foi o {maior} encontrado na posição {posmaior}')