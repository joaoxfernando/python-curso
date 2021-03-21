'''
ler nome e media de um aluno
guardando tbm a situação em um dicionário
no final mostre a estrutura na tela
'''
ficha = {'Nome': input('Digite o nome: '), 'Média': float(input('Digite a média do aluno: '))}

if ficha['Média'] < 6:
    ficha['Situação'] = 'Reprovado'
elif 5 <= ficha['Média'] < 7:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Aprovado'

print('*'*25)
for c, v in ficha.items():
    print(f' - {c:10}: {v}.')