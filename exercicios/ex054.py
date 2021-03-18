'''
Ler data de nasc de 7 pessoas
no final mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores
'''

from datetime import date
ano = date.today()
maiores = 0
menores = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de seu nascimento com 4 dígitos: '))
    if ano.year - nasc >= 21:
        maiores += 1
    else:
        menores += 1
print('Temos um total de {} maiores e {} menores de idade.'.format(maiores, menores))