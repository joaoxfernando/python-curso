'''
programa com função ficha() que receba os parametros:
nome de jogador e gols marcados
o programa deve ser capaz de mostrar a ficha do jgoador mesmo que algum dado
não tenha sido informado corretamente
'''

def ficha(nome, gols=0):
    print('-' * 50)
    print(f'{"Ficha do jogador "}{nome}')
    print(f'{"Nome:"}{nome:^45}')
    print(f'{"Gols: "}{gols:^45}')


nome = str(input('Digite o nome do jogador: '))
gols = int(input(f'Digite quantos gols {nome} marcou: '))
ficha(nome, gols)