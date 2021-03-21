'''
gerenciar aproveitamento de jogador de futebol
prog vai ler nome e quantas partidas ele realizou
depois ler gols em cada partida.
no final tudo será guardado em um dicionário incluindo gols feitos no camp.

'''

jogador = {'nome': input('Nome do jogador: ')}
partidas = list()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, jogador['partidas']):
    partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(jogador['gols'])
jogador['média'] = jogador['total'] / jogador['partidas']
print("<>"*25)
print(f'{jogador["nome"]} marcou um total de {jogador["total"]} gols em {jogador["partidas"]} partidas.')
print(f'E a média de gols de {jogador["nome"]} é de {jogador["média"]:.2f} gols por partida.')
