'''
função area que vai receber as dimensões (largura e comprimento)
de um terreno retangular e mostre a área do terreno.
'''
def linha():
    print('-' * 45)


def calcularArea(a, b):
    area = a * b
    print(f'Dimensões do terreno: ')
    print(f'Largura: {a}')
    print(f'Comrpimento: {b}')
    print(f'A área desse terreno é de: {area:.2f}m².')


linha()
print(f'{"CALCULAR ÁREA DE TERRENO RETANGULAR":^45}')
linha()
while True:
    largura = input('Largura (m): ')
    if not largura.isnumeric():
        print('Digite apenas números!')
    else:
        break
while True:
    comprimento = input('Comprimento (m): ')
    if not comprimento.isnumeric():
        print('Digite apenas números!')
    if comprimento == largura:
        print(f'O comprimento não pode ser igual a largura ({largura}) metros. Digite novamente')
    else:
        break
calcularArea(int(largura), int(comprimento))