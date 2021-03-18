'''
ler sexo da pessoa
aceitar apenas F ou M
Se digitar outra coisa, pedir para digitar novamente
'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo: [M/F] ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Opção inválida, tente novamente.')
print('Obrigado!')