'''
melhorar o 61
perguntando se deseja mostrar mais X termos...
só vai parar quando digitar 0
'''
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
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total :
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você deseja mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))