'''
tenha tupla contagem por extenso, de zero a vinte.
seu programa deverá ler um número pelo teclado e mostra-lo por extenso.
'''

numero = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 0 a 20: '))
while True:
    if num <= 0 or num > 20:
        num = int(input('Número inválido, tente novamente: '))
    else:
        print(f'Você digitou o número {numero[num-1]}.')
        break