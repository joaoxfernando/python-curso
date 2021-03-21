'''
contagem regressiva para fogos.
de 10 a 0
com pausa de 1 seg entre eles...
'''

from time import sleep
from emoji import emojize

print('Prepare-se para a contagem regressiva..')
for c in range(10, 0, -1):
    print('{}'.format(c))
    sleep(1)

print(emojize(':fireworks:'))
sleep(1)
print('Feliz ano novo!')