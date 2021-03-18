'''
ler varios nueros e colocar numa lista
mostre:
a - quantos numeros foram digitados
b - a lista ordenada de forma decrescente
c - se o valor 5 foi digitado e está presente na listsa
'''

lista = []
continuar = 'S'

while True:
    lista.append(int(input('Digite um número: ')))
    if continuar == 'N':
        break
    else:
        continuar = str(input('Quer continuar? [S/N]')).upper()[0]
        if continuar == 'N':
            break

print(f'Foram digitados ao todo {len(lista)} números!')
print(f'Os números digitados em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 foi digitado na lista.')
else:
    print('O número 5 não foi digitado e não está na lista')