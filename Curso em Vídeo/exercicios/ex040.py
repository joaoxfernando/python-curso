'''
duas notas - calcular media
< 5 - reprovado
> 5 e < 7 - recuperação
7 ou mais - aprovado
'''


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Você ficou com nota {:.2f} de média e está reprovado'.format(media))
elif media < 6.9:
    print('Você ficou com nota {:.2f} de média e está de recuperação'.format(media))
else:
    print('Parabéns, sua média foi {:.2f} e você foi aprovado!'.format(media))