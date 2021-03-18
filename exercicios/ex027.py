nome = input('Digite o seu nome completo: ')

nome_dividido = nome.split()
firstname = nome_dividido[0]
lastname = nome_dividido[-1]

print(firstname)
print(lastname)