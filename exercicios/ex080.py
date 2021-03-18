'''
criar programa que usuario digita 5 valores numericos
já na ordem correta de inserção sem usar o sort()
no final mostrar a lista na ordem correta..
'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        print(f'Número adicionado ao final da lista.')
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Número adicionado na posição {pos+1}.')
                break
            pos += 1

print(f'Os valores digitados em ordem crescente são: {lista}')