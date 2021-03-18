
'''
Natação categorias de acordo com idade:
calcular idade pelo ano de nascimento
até 9 anos - mirim
até 14 anos infantil
até 19 anos junior
até 20 senior
> master
'''

from datetime import date

ano = int(input('Digite o ano de nascimento: '))
agora = date.today()
idade = agora.year - ano

if idade < 9:
    print('Você tem {} anos e está na categoria mirim.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria infantil.'.format(idade))
elif idade <= 19 :
    print('Você tem {} anos e está na categoria júnior'.format(idade))
elif idade <= 20:
    print('Você tem {} anos e está na categoria senior.'.format(idade))
elif idade > 20:
    print('Você está na categoria sênior')