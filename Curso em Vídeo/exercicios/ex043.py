'''
Programa que lê altura, peso e calcula o IMC.
'''

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? (em metros)'))


imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >=18.5 and imc < 25:
    print('Parabéns, você está no seu peso ideal.')
elif imc > 25 and imc <= 30:
    print('Alerta! Você está com sobrepeso!')
elif imc > 30 and imc <= 40:
    print('CUIDADO! Você está com OBESIDADE!')
else:
    print('VOCÊ ESTÁ COM OBSEIDADE MÓRBIDA! \nAconselho a procurar um médico')