
print('qual sera a base de convesão')
print('                             ')
print('Conversão para Binário opção 1')
print('                             ')
print('Conversão para Octal opção 2')
print('                             ')
print('Conversão para Hexadecimal opção 3')
opc = int((input('Qual opção: ')))
numero= int(input('Digite o numero: '))


if opc == 1:
 bina = bin(numero)[2:]
 print(bina)
elif opc == 2:
 octal = oct(numero)[2:]
 print(octal)
elif opc == 3:
 hexadecimal = hex(numero)[2:]
 print(hexadecimal)
else:
 print('NÃO TEM ESSA OPÇÃO')

