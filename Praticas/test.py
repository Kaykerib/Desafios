print("==== Casa das Tintas ====")

l = float(input('Diga qual é a Largura da parede: '))
a = float(input('Diga qual a Altura da parede: '))

#função
def area(l,a):
 z = f'{l} + {a} = { l + a}'
 return z

def quadrado(l,a):
 q = f'{l} x {a} = { l * a}'
 return q

def lata(l,a):
 r = 2
 s = (l * a) / r
 return int(s)

print('A Area da parede é',(area(l,a)))
print(f'Entao ela tem ao,{(quadrado(l,a))} m²')
print(f'Para pinta a parede serão necesarias {lata(l,a)} latas')