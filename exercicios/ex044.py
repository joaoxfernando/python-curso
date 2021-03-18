'''
calcular valor a ser pago por um produto com as condições abaixo:
- a vista dinheiro/cheque 10% desconto
- a vista cartao 5%
- em até 2x cartão preço normal
- 3x ou mais 20% juros
'''

valor = float(input('Digite o valor do produto: '))
print('''==== Escolha uma das seguintes opções de pagamento ====
A VISTA DINHEIRO/CHEQUE: digite 1
A VISTA NO CARTÃO: digite 2
Parcelar em 2x no cartão: Digite 3
Para parcelar em 3x: Digite 4''')
opcao = int(input('Digite a opção: '))
valorfinal = 0

if opcao == 1:
    valorfinal = valor - (valor * 10 / 100)
elif opcao == 2:
    valorfinal = valor - (valor * 5 / 100)
elif opcao == 3:
    valorfinal = valor
else:
    valorfinal = valor + (valor * 20 / 100)

print('O valor final do produto será de: R$ {}'.format(valorfinal))