import urllib
import urllib.request
endereço = str(input('Digite o endereço do site que deseja consultar (com http://) '))
try:
    site = urllib.request.urlopen(endereço)
except urllib.error.URLError:
    print('O site não está acessível!')
else:
    print(f'Consegui acessar o site: {endereço} com sucesso.')