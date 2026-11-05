ladoa = float(input('tamanho do lado A: '))
ladob = float(input('Tamanho do lado b: '))
ladoc = float(input('Tamanho do comprimento: '))


triangulo = ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob

if triangulo:
 print(f' \033[7;30m Da para monta o triangulo \033[m')


 if ladoa == ladob == ladoc:
    print(f'equi') 

 elif ladoa == ladob or ladoa == ladoc or ladob == ladoc: 
 
   print(f'iso')

 else:

    print(f'esca')

else:
   
  print(f'\033[34m Não monta o triangulo \033[m ')
