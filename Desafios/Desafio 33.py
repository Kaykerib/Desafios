n1 = int(input('Primeiro 1: '))
n2 = int(input('Segundo 2: '))
n3 = int(input('Terceiro 3: '))

if n1 >= n2 and n1 >= n3:
 maior = n1
elif  n2 >= n1 and n2 >= n3:
 maior = n2
else:
 maior = n3

if n1 <= n2 and n1 <= n3:
 menor = n1
elif  n2 <= n1 and n2 <= n3:
 menor = n2
else:
 menor = n3 

print(f' \033[35m Numero maior{maior}\033[m , \033[36m Numero menor{menor}\033[m')