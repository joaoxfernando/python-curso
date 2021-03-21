def soma(a, b):
    s = a + b
    print(f'A soma entre {a} + {b} é igual a {s}')


soma(5, 3)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 0, 3, 9]
dobra(valores)
print(valores)
