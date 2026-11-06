from math import hypot
op = int(input('digite o numero do cateto oposto: '))
ad = int(input('digite o numero do cateto adjecente: '))

hipotenusa = hypot(op,ad)

print(f'A hipotenusa é: \033[31m{hipotenusa}\033[m')