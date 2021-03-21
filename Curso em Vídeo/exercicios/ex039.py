from datetime import date

ano = int(input('Digite o ano de nascimento:' ))
hoje = date.today()
idade = hoje.year - ano
resto = 18 - idade
passou = idade - 18
if idade < 17:
    print('Ainda não precisa se alistar, mas faltam {} anos para se alistar.'.format(resto))
elif idade == 17:
    print('Ainda não precisa se alistar, mas falta {} ano para se alistar.'.format(resto))
elif idade == 18:
    print('Já está na hora de se alistar.')
elif idade == 19:
    print('Já passou do tempo de se alistar. Você está {} ano atrasado.'.format(passou))
else:
    print('Já passou do tempo de se alistar. Você está {} anos atrasado.'.format(passou))