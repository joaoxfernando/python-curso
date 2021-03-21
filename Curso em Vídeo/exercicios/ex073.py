'''
criar tupla com os 20 primeiros colocados do brasileirão na ordem de colocação
depois mostre:
a - apenas os 5 primeiros colocados.
b - os últimos 4 colocados
c - uma lista com os times em ordem alfabética
d - a posição na tabela do time da chapecoense.
'''

times = ('São Paulo', 'Grêmio', 'Cruzeiro', 'Palmeiras', 'Flamengo', 'Internacional', 'Botafogo', 'Goiás', 'Coritiba',
         'Vitória', 'Sport', 'Atlético-MG', 'Atlético-PR', 'Fluminense', 'Santos', 'Náutico', 'Figueirense',
         'Vasco da Gama', 'Portuguesa', 'Ipatinga')

print('='*20)
print(f'Os vinte clubes participantes do Brasileirão de 2008 e em ordem alfabética foram: \n{sorted(times)}')
print('='*20)
rebaixados = times[16:]
print(rebaixados)
print(f'Os cinco primeiros colocados do campeonato foram: {times[0:5]}')
print(f'Os quatro últimos foram {times[16:]} e foram rebaixados.')

pesquisar = str(input('Qual clube você deseja saber a posição? ')).capitalize()
print(f'O Cruzeiro ficou na {times.index((pesquisar))+1}ª posição.')