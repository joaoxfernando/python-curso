'''
criar tupla com varias palavras (sem acentos)
depois deve mostrar para cada palavra, quais as vogais...
'''

palavras = ('Notebook',
         'Computador',
         'Smartphone',
         'Tablet',
         'Monitor',
         'Teclado',
         'Mouse',
         'Headset')

for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem como vogais: ', end='')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(letra, end=' ')