'''
criar programa para ler vários números
cadastre numa lista
caso num já exista, ele nao sera adicionado
no final serão exibidos todos valores únicos em ordem crescente
'''
lista = []
continuar = 'S'
while True:
    # c += 1
    num = int(input('Digite um valor: '))
    if continuar == 'N':
        break
    if num in lista:
        print(f'Valor duplicado. Não vou adicionar...')
        continuar = str(input('Quer continuar? [S/N] ')).upper()
        if continuar == 'N':
            break
    else:
        lista.append(num)
        print('Valor adicionado com sucesso.')
        continuar = str(input('Quer continuar? [S/N] ')).upper()
        if continuar == 'N':
            break
if len(lista) > 1:
    lista.sort()
    print(f'Os valores digitados foram: {lista}')
else:
    print(f'O único valor digitado foi: {lista}')