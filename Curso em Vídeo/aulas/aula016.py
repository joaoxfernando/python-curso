# TUPLAS
lanches = ('Hamburger', 'Batata frita', 'Cachorro quente', 'Pudim')

for comida in lanches:
    print(f'Eu vou comer {comida}')
print('Delicia!')

a = (2, 5, 3)
b = (4, 8, 9, 1, 3)
c = a + b
print(c)
print(sorted(c)) # organiza numa lista em ordem alfabética/crescente
print(c.index(3)) # mostra a primeira ocorrência do número 3
print(c.count(9)) # quantas vezes aparece o número '9'

pessoa = ('João Fernando', 32, 'M', 70.1)
print(f'O nome é {pessoa[0]}, tem {pessoa[1]} anos e pesa {pessoa[3]} kgs.')