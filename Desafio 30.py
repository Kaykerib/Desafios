n = int(input('Digite o numero para descobri se é impa ou par: '))



resto = n % 2 

if resto == 0:
 resultado = 'par' 
else:
 resultado = 'impar'

print(resultado)
