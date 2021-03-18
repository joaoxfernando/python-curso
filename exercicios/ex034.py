'''
perguntar salário de funcionário e calcular valor do aumento
salarios > 1250 o aumento será de 10%
se <= o aumento será de 15%
'''

salario = int(input('Digite o valor do seu salário: '))

if salario > 1250:
    aumento = 0.10
else:
    aumento = 0.15

novoSalario = salario*(1+aumento)
print('O novo salário será de: {}'.format(novoSalario))