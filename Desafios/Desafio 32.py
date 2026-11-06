ano = int(input('Digite um ano bixesto ex:20XX: '))
resto = ano % 4 and ano % 100 != 0 or ano % 400 == 0  
if resto == 0:
 resultado = 'Ano bissexto'
else:   
 resultado = 'Não bissexto'
print(f'\033[34m resultado \033[m ')