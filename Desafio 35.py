ladoa = float(input('tamanho do lado A: '))
ladob = float(input('Tamanho do lado b: '))
comprimento = float(input('Tamanho do comprimento: '))

soma = ladoa + ladob 

if soma >= comprimento:
 print(f' \033[7;30m Da para monta o triangulo \033[m')
else:
 soma < comprimento     
 print(f'\033[34m Não monta o triangulo \033[m ')

