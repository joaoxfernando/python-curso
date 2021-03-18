'''
programa para saber se ano é BISSEXTO
'''
from datetime import date
ano = int(input('Digite o ano para verificar se ele é bissexto. '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))