'''
ler quatro valores e guarde-os em uma tupla
no final mostre:
a quantas vezes apareceu o valor 9
b em que posição foi digitado o primeiro valor 3
c quais foram os numeros pares
'''

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')))

print(f'Os valores digitados foram: {num}')
if 3 in num:
    print(f'O número tres digitado a primeira vez na {num.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado nenhuma vez.')
if num.count(9) > 1:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
elif num.count(9) == 1:
    print(f'O valor 9 apareceu {num.count(9)} vez.')
else:
    print(f'O valor 9 não foi digitado nenhuma vez.')
print(f'Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')