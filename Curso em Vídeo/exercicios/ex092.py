'''
ler nome, ano de nasc, carteira de trab e cadastre-os em um dicionário
se a ctps for direferente de 0 o dicionário deverá ler salario e ano de contrataçao
calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar
'''
from datetime import datetime
ficha = {}
ficha['nome']  = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
ficha['idade'] = datetime.now().year - nasc
ficha['cpts'] = int(input('CTPS: (0 se não tiver) '))
if ficha['cpts'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: '))
    ficha['apos'] = ficha['idade'] + ((ficha['contratação'] + 35) - datetime.now().year)

print(f'Nome: {ficha["nome"]}')
print(f'Idade: {ficha["idade"]} anos.')
if ficha['cpts'] == 0:
    print(f'{ficha["nome"]} ainda não tem carteira de trabalho.')
else:
    print(f'Ano de cntratação: {ficha["contratação"]}.')
    print(f'Se aposentará aos: {ficha["apos"]} anos.')