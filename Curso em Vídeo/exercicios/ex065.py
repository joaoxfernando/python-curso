'''
ler varios numeros
mostre a media entre todos
e qual foi o maior e qual o menor
o programa deve perguntar se deseja continuar a digitar valores ou não
'''

from time import sleep

soma = cont = media = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    n = int(input('Digite um  número: '))
    soma += n
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
print('CALCULANDO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
if maior == menor:
    print('Tanto o maior quanto o menor número foram iguais: {}'.format(maior))
else:
    print('O menor número digitado foi: {}'.format(menor))
    sleep(1)
    print('E o maior número digitado foi: {}'.format(maior))
sleep(1)
print('A média entre os números digitados é igual a: {:.2f}'.format(media))