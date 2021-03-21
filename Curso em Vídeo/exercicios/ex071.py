'''
simular caixa eletronico
escolher valor de saque
contar quantas cedulas ira fornecer de cada valor
cedulas de 50, 20, 10 e 1.
'''
banco = 'Banco JF'

print('='*26)
print('{:^26}'.format(banco))
print('='*26)
valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
cedula = 50
totalced = 0

while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced >= 1:
            print(f'Total de {totalced} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
print('='*26)
print(f'Volte sempre ao Banco {banco}.')