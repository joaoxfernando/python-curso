'''
leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão.
'''

print('='*30)
print('      10 TERMOS DE UMA PA')
print('='*30)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
decimo = termo + (10-1) * razao

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
    # if cont == 10:
    #     print('Quer continuar? ')
print('ACABOU!')