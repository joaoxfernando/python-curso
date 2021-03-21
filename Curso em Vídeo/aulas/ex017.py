a = [2, 3, 8, 1]
b = a
print(f'Lista A: {a}\nLista B: {b}')
b[3] = 3
print(f'Lista A: {a}\nLista B: {b}')
c = [5, 3, 0, 7]
d = c[:]
print(f'Lista C: {c}\nLista D: {d}')
d[2] = 5
print(f'Lista C: {c}\nLista D: {d}')