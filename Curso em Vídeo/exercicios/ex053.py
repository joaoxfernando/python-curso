'''
ler um frase qualquer e diga se ela é
PALÍNDROMO, ou seja, se é possível ler de trás para frente
DESCONSIDERANDO OS ESPAÇOS

"RETIRAR ESPAÇO DAS FRASES"

exemplos:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

print('-=-='*6+'-')
print(' Detector de palíndromos')
print('-=-='*6+'-')
frase = str(input('Digite uma frase: ')).strip()
frasetratada = frase.upper()
palavras = frasetratada.split()
junto = ''.join(palavras)
inverso = junto[::-1].upper() # o comando ::-1 começa a frase do último caractere voltando de 1 em 1.

print('O inverso da frase {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')