viagem = float(input('quanto km e a sua viagem: '))


if viagem <=200:
 r = 0.50 * viagem

else:
 r = 0.45 * viagem
 

print(f' \033[35m A viagem vai custa {r} \033[m ')

