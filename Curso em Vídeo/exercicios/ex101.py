'''
programa para mostrar se voto é obrigatório
'''
from datetime import datetime
def voto(nasc):
    """
    >> Calcula se com a idade atual a pessoa já pode votar e se é obrigatório ou opcional.
    :param nasc: ano de nascimento com 4 digitos.
    :return: não é necessário.
    """
    ano = datetime.now().year
    idade = ano - nasc
    if idade < 16:
        print(f'Com {idade} anos não pode votar!')
    elif idade >= 16 and idade < 18 or idade > 65:
        print(f'Com {idade} anos o voto é opcional.')
    else:
        print(f'Com {idade} anos o voto é OBRIGATÓRIO.')


nasc = int(input('Digite o ano de nascimento com 4 dígitos: '))
voto(nasc)

help(voto)