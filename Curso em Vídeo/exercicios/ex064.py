'''
ler varios numeros inteiros
so vai parar qnd digitar 999
no final mostre quantos numeros foram digitados e a soma entre todos eles
(desconsiderando o 999)
'''

flag = False
soma = cont = 0
print('''================================\nSOMADOR DE NÚMEROS
Caso queira concluir a soma, é só digitar 999''')
print('='*32)
while flag == False:
  num = int(input('Digite um número: '))
  if num == 999:
    flag = True
  else:
    soma += num
    cont += 1
print('Você digitou um total de {} números.'.format(cont))
print('E a soma de todos os números digitados é igual a {} '.format(soma))