'''
converter numero inteiro para:
binario
octal
hexadecimal
'''

num = int(input('Digite o número inteiro que deseja converter: '))
print('''Digite a opção que deseja converter:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input('Digite uma das opções acima: '))

if opcao == 1:
    print('O valor {} convertido para binário é igual a: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O valor {} convertido para octal é igual a: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O valor {} convertido para hexadecimal é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')