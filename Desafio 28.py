import random
n = int(input('Adivinhe um numero de 0 a 5: '))
p = [0,1,2,3,4,5]
s = random.choice(p)
#The choice() method returns a randomly selected element from the specified sequence

if n == s:
    print(f'\033[32m acertou \033[m ')
else:
 print(f' \033[31m Não acertou {s} \033[m')   
    

