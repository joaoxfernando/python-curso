'''
4 jogadores joguem um dado e tenham resultados aleatórios.
guarde esses resultados em um dicionário.
coloque em ordem sabendo que o vencedor tirou o maior número no dado
'''
from operator import itemgetter
from random import randint
from time import sleep
players = { 'Player 1': randint(1, 6),
            'Player 2': randint(1, 6),
            'Player 3': randint(1, 6),
            'Player 4': randint(1, 6)}
print('Valores sorteados:')
for c, v in players.items():
    print(f'O {c} tirou {v} no dado.')
    sleep(1)
ranking = {}
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('RANKING')
for c, v in enumerate(ranking):
    print(f'{c+1}º lugar {v[0]} com {v[1]} pontos.')
    sleep(1)