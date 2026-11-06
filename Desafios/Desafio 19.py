import random
a = (input('Digite o nome do aluno 1: '))
b = (input('Digite o nome do aluno 2: '))
c = (input('Digite o nome do aluno 3: '))
d = (input('Digite o nome do aluno 4: '))

alunos=[a,b,c,d]
#The choice() method returns a randomly selected element from the specified sequence.
aleatorio = random.choice(alunos)
print(f'\033[32m {aleatorio}\033[m')