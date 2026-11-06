
#apenas letras e números (de A-Z, a-z e 0-9), incluindo letras com acentos.
n=(input('\033[31m valor \033[m'))
print(n.isalnum())

#verificar se todas as letras do texto estão em maiúsculas.
n=(input('valor'))
print(n.isupper())

#Se digitar apenas letras sem acento, números e espaços, o resultado será True.
n=(input('valor: '))
print(n.isascii())