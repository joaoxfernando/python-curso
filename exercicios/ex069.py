'''
ler idade e sexo
a cada pessoa cadastrada, perguntar se quer continuar
no final mostrar:
a - quantas pessoas > 18 anos
b - quantos homens foram cadastrados
c - quantas mulheres < 20 anos.
'''

mais18 = homens = mulheres = idade = 0
sexo = ''
continuar = 'S'
while continuar in 'Ss':
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo? [M/F]: ')).upper().strip()[0]
    print('-'*36)
    continuar = str(input('Quer continuar a cadastrar? [S/N]: ')).upper().strip()[0]
    print('-'*36)
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if continuar == 'N':
        break

print(f'Foram cadastradas {mais18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados um total de {homens} homens.')
print(f'Foram cadastradas um total de {mulheres} mulheres abaixo de 20 anos.')