def fatorial(num, show):
    f = 1
    if show:
        print(f'O fatorial de {num} é igual a: ', end='')
    else:
        print(f'O fatorial de {num} é: ', end='')
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            elif c == 1:
                print(f'{c} = ', end='')
    print(f)

n = int(input('Digite um número para ver o seu fatorial: '))
show = str(input('Deseja mostrar o cálculo do fatorial? [S/N] '))[0]
if show in 'Ss':
    show = True
else:
    show = False

fatorial(n, show)