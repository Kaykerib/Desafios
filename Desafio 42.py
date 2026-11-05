ladoa = float(input('tamanho do lado A: '))
ladob = float(input('Tamanho do lado b: '))
ladoc = float(input('Tamanho do comprimento: '))

soma = ladoa + ladob 
triangulo = soma >= ladoc

if triangulo:
 print(f' \033[7;30m Da para monta o triangulo \033[m')


elif ladoa == ladob or ladoc:
 print(f'equi') 

elif ladoa == ladob or ladoa == ladoc or ladob == ladoc: 
 
 print(f'iso')

elif ladoa != ladob != ladoc:

 print(f'esca')

else:
  soma < ladoc     
  print(f'\033[34m Não monta o triangulo \033[m ')
