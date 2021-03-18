'''
ler a velocidade do carro
se ultrapassar 80kmh, mostrar msg alertando sobre multa
a multa custa 7 reais por cada km acima.
'''
print('='*20)
print('ATENÇÃO AO RADAR!')
print('='*20)

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print('Você foi multado por ultrapassar o limite de velocidade. \nSua multa será de R${} '.format(multa))
else:
    print('Parabéns, você está dentro dos limites de velocidade.')