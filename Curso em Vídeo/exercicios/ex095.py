'''
aprimorar ex 093.
permitir cadastrar mais de um jogador
incluir sistema de visualizar detalhes de aproveitamento de cada jogador.
'''

time = list()
partidas = list()
jogador = dict()
while True:
    jogador.clear()
    jogador = {'nome': input('Nome do jogador: ').title()}

    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for p in range(0, jogador['partidas']):
        partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = partidas[:]
    # jogador['total'] = sum(jogador['gols'])
    # jogador['média'] = jogador['total'] / jogador['partidas']
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S / N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*45)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*45)
for c, v in enumerate(time):
    print(f'{c+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*45)

while True:
    busca = int(input('Mostrar qual jogador? [999 parar] ')) - 1
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. Não existe jogador com o código {busca+1}')
    else:
        print(f'--- ESTÁTISTICAS DO JOGADOR "{time[busca]["nome"].upper()}":')
        for i, g in enumerate(time[busca]["gols"]):
            if g > 1:
                print(f'   Na {i+1}ª partida {jogador["nome"]} marcou {g} gols.')
            elif g == 1:
                print(f'   Na {i+1}ª partida {jogador["nome"]} marcou {g} gol.')
            else:
                print(f'   Na {i+1}ª partida {jogador["nome"]} não marcou gol.')
    print('-'*45)
print('<> VOLTE SEMPRE! <>')
