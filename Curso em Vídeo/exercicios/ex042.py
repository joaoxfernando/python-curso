'''exercicio dos triangulos + aprimorado

equilatero = 3 lados iguais
isosceles = dois lados iguais
escaleno = todos lados diferentes

'''

'''
ler comprimento de tres retas
dizer se elas podem ou não formar um triângulo
'''

seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima podem formar um triângulo.')
    if seg1 == seg2 == seg3:
        print('O triângulo será equilatero.')
    elif seg1 != seg2 != seg3 != seg1:
        print('O triângulo será escaleno.')
    else:
        print('O triângulo será isósceles.')
else:
    print('Os segmentos acima não podem formar um triângulo.')

