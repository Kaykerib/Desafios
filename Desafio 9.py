n1 = int(input('Digite um numero para fazer a tabuada: '))



def soma(x,i):
 
 r = f'{x} x {i} = {x * i}'
 s = f'{x} + {i} = {x + i}'
 return r,s

cores={'limpa' :'\033[m',
        'roxo':'\033[35m',
        'azul marinho' :'\033[36m',
        'azul' :'\033[34m'}

for i in range(n1,10):
 resultado = soma(n1, i)

 print('{}{}{} x {}{}{} = {}{}{} '.format(
  cores['azul marinho'],n1,cores['limpa'],
  cores['azul marinho'], i ,cores['limpa'],
  cores['azul'],resultado,cores['limpa']))


