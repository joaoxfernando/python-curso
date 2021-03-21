money = float(input('Digite um valor em reais: R$ '))
cotação = float(input('Digite a cotação do dólar: '))
dolar = money/cotação

print(f'Você tem R$: {money}\nSe quiser você pode comprar até US$: {dolar}\nA cotação do dólar é de R$ {cotação}')