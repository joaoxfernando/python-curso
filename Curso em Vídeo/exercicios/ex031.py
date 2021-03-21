'''
perguntar distancia da viagem:
se > 200km o custo por km será de 0.45
se < o custo será de 0.50
'''

distancia = int(input('Digite a distância da sua viagem em km: '))

if distancia > 200:
    preco = 0.45 * distancia
else:
    preco = 0.50 * distancia

print('O preço da sua viagem será de: R$ {}'.format(preco))