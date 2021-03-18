# Programa que calcula a área e a quantidade de tinta necessária para pintá-la.
# Cada litro de tinta pinta 2m²

altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largura da parede: '))

area = altura*largura
tinta = area/2

print('A área da parede é de: {}\nE será necessário {} litros de tinta para pintá-la'.format(area, tinta))