p = float(input('Qual é o preço do produto? '))

r = (p * 0.05) - p
po = abs(r) 


print(f'O produto fica um no valor de \033[34m {po}\033[m com 5% de desconto')