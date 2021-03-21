nome = str(input('Qual o seu nome? '))

tam = len(nome) - nome.count(' ')

print('Em letras maíusculas: {} '.format(nome.upper()))
print('Em letras minusculas: {}'.format(nome.lower()))
print('O nome {} tem um total de {} letras'.format(nome, tam))
print('O primeiro nome tem um total de {} letras'.format(nome.find(' ')))