# Calcular o salário com um aumento de 15%
# Para alterar a porcentagem de aumento, lembre-se de deixá-la convertida em %
# 15% = 0.15 - Se for 5% = 0.05

salario = int(input('Digite o salário: '))
fator = 0.15
aumento = salario*fator
novoSalario = salario+aumento

print('O salário é de R${}\nO aumento será de R$ {}\nCom o aumento o novo salário será de R${}'.format(salario, aumento, novoSalario))