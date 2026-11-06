n = input('Digite o nome completo')  
p = n.split()[0]
s = n.split()[-1]
#O índice [-1] aponta sempre diretamente para o último elemento de qualquer lista.
print(f'\033[36m {p,s} \033[m')