'''
tabuada de vários números
1 de cada vez para cada valor digitado
só vai parar quando o número digitado for negativo.
'''

while True:
    num = int(input('Você quer ver a tabuada de qual valor: (0 para interromper) '))
    print('='*20)
    if num <= 0:
        break
    for cont in range(1,11):
        print(f'{num} x {cont} = {num*cont}')
    print('='*20)
print('PROGRAMA TABUADA ENCERRADO.')