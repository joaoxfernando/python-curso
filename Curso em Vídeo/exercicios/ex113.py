def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2:.1f}.')