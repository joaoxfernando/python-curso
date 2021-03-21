'''
ler nome, sexo e idade de várias pessoas e guardar os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista..
no final mostre:
a - quantas pessoas foram cadastradas
b - a média de idade do grupo
c - uma lista com todas as mulheres
d - uma lista com todas as pessoas com idade acima da média
'''
pessoas = dict()
todos = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Digite o nome: '))
    while True:
        pessoas['sexo'] = str(input('Digite o sexo: [F/M] ')).upper()[0]
        if pessoas['sexo'] in 'MmFf':
            break
        print('Erro! Digite apenas M ou F.')
    pessoas['idade'] = int(input('Digite a idade: '))
    soma += pessoas['idade']
    todos.append(pessoas.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if continuar in 'Nn':
        break

print(todos)
media = soma / len(todos)

print(f'Foram cadastradas ao todo {len(todos)} pessoas.')
print(f'A média de idade do grupo é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for t in todos:
    if t['sexo'] == 'F':
        print(f'{t["nome"]} ', end='')
print('\nAs pessoas acima da média foram: ')
for t in todos:
    if t['idade'] > media:
        print('    ', end='')
        for c, v in t.items():
            print(f'{c}: {v}; ', end='')
        print()
print('ENCERRADO')