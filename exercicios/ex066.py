'''
ler varios número
só para qnd digitar 999
no final mostra qnts numeros digitados e a soma entre eles, desconsiderando o flag
'''

soma = cont = num = 0

while True:
    num = int(input('Digite um número. [999 para cancelar]:  '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'Você digitou um total de {cont} números e a soma entre todos eles é de {soma}. ')