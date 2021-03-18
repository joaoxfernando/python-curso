'''
ler três números e mostrar qual deles é o maior e qual o menor
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

def checarMaior():
    if n1>=n2 and n1>=n3:
        maior = n1
    elif n2>=n1 and n2>=n3:
        maior = n2
    else:
        maior = n3
    print('O maior número é o {}'.format(maior))

def checarMenor():
    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3
    print('O menor número é o {}'.format(menor))

checarMaior()
checarMenor()