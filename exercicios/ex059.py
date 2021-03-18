'''
ler dois valores
mostrar menu contendo:
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair
realizar a operação dos dois numeros conforme opção escolhido
'''

opcao = 4
soma = mult = 0
maior = menor = 0
if opcao != 5:
  while opcao == 4:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('''Menu de Opções
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    opcao = int(input('Escolha uma das opções acima: '))
  if opcao == 1:
    soma = n1 + n2
    print('{} + {} = {}'.format(n1, n2, soma))
  elif opcao == 2:
    mult = n1 * n2
    print('{} x {} = {} '.format(n1, n2, mult))
  elif opcao == 3:
    if n1 > n2:
        maior = n1
        menor = n2
        print('O maior número é o {} e o menor é o {}'.format(maior, menor))
    elif n1 == n2:
        print('Os números são iguais')
    else:
        menor = n1
        maior = n2
        print('O maior número é o {} e o menor é o {}'.format(maior, menor))
if opcao == 5:
  print('Você preferiu sair do programa.')

print('\nObrigado e volte sempre')