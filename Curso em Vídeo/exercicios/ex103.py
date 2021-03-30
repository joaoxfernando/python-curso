'''
programa com função ficha() que receba os parametros:
nome de jogador e gols marcados
o programa deve ser capaz de mostrar a ficha do jgoador mesmo que algum dado
não tenha sido informado corretamente
'''

def ficha(nome, gols=0):
    print('-' * 50)
    print(f'O jogador {nome} fez {gols} gols.')


nome = str(input('Digite o nome do jogador: '))
if nome == '':
    nome = '<desconhecido>'
gols = str(input(f'Digite a quantidade de gols marcados: '))
if gols.isnumeric() == True:
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)