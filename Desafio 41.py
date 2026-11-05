print(f'\033[35m Confederação Nacional de Natação \033[m')
idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print('Mirim')
elif idade <= 14:
  print('Infatil')
elif idade <= 19:
  print('Junior')
elif idade <= 20:
   print('Sênior')
else:
  print('Master')
