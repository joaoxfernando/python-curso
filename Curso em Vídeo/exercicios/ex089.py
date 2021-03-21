'''
ler nome e duas notas de vários alunos
no final mostrar boletim contendo a media de cada um
e permitir que usuario possa ver as notas de cada aluno individualmente
'''
from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))[0]
    if resp in 'Nn':
        break


print('='*8, 'BOLETIM', '='*8)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))-1
    if opc == 998:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print('Consultando...')
        sleep(1)
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('>>> VOLTE SEMPRE <<<')