'''
digitar uma expressão que use parenteses
analisar se a expressão esta com os parenteses digitados na ordem correta
'''

exp = str(input('Digite a expressão: '))
pilha = []
for parenteses in exp:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão foi válida.')
else:
    print('Sua expressão foi inválida.')