'''
empréstimo p/ compra de uma casa:
valor da casa
salario
anos para pagar
'''

valor = float(input('Digite o valor da casa que quer financiar: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos deseja pagar o financiamento: '))
prestacao = valor / (anos * 12)
limite = salario * 0.3

if prestacao > limite:
    print('Não podemos fazer o empréstimo pois o valor da prestação será superior à 30% do seu salário.')
    print('O valor da prestação para esse prazo deverá ser de: R${:.2f}'.format(prestacao))
    print('E o valor do seu limite para empréstimo de acordo com seu salário é de: R${:.2f}'.format(limite))
else:
    print('O empréstimo foi aprovado. A prestação será de: {:.2f}'.format(prestacao))
    print('O seu limite para empréstimo de acordo com a sua renda é de: R${:.2f}'.format(limite))