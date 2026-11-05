n = input("digite o nome completo: ")
print(n.upper())
print(n.lower())

r = n.replace(" ","")
print(f'\033[37m {len(r)}\033[m')

 
p = n.split()[0]
print(f'\033[34m {len(p)} \033[m')