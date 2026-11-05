salario = int(input('Digite o seu salario: '))

if salario <= 1250:
 calculo = 0.15 * salario
 resul = salario + calculo

else:
 calculo = 0.10 * salario
 resul = salario + calculo
print(f' 033[32m O Seu salario com o aumento ficou {resul:.2f} \033[m ')
