# Ler o preço de um determinado produto e mostrar o novo valor com desconto.
# O desconto utilizado é de 5% - Se desejar mudar é so alterar a variável 'fator'
# A variável fator está já convertida em %, logo 5% = 0.05 - Se for 50% o valor deve ser 0.50

valor = int(input('Digite o valor do produto: '))
fator = 0.05
desconto = valor*0.05
novoValor = valor - desconto

print('O valor do produto é de R$ {}\nO desconto é de R${}\nSeu novo valor já com o desconto aplicado é de R${}'.format(valor, desconto, novoValor))