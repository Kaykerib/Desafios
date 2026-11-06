print('===Calculo IMC === ')
altura = float(input('Qual é a Altura'))
peso = float(input('Qual e o Peso'))

imc =  peso / (altura * altura) 

if imc < 18.5:
    print('Voce estar abaixo do Peso')
elif imc > 18.5 and imc <= 25:
    print(f' \033[32m Estar no peso ideal \033[m') 
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')