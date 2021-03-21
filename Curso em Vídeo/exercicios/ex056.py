'''
ler nome, idade e sexo de 4 pessoas
no final mostre:
A média de idade
Nome do homem mais velho
Quantas mulheres tem menos de 20 anos.
'''
velho = ''
mulheres = 0
maisvelho = 0
somaidade = 0
for c in range(1, 5):
    print('--- {}ª PESSOA ---'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    somaidade += idade

    if sexo == 'M' and c == 1:
        velho = nome
        maisvelho = idade
    elif sexo == 'M' and idade > maisvelho:
        velho = nome
        maisvelho = idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
media = somaidade/(c)
print('A média de idade é de {:.2f} anos'.format(media))
print('O homem mais velho é o {} com {} anos.'.format(velho, maisvelho))
print('O total de mulheres com menos de 20 anos é de: {}'.format(mulheres))