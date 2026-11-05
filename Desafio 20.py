import random
a = (input('Digite o nome do aluno 1: '))
b = (input('Digite o nome do aluno 2: '))
c = (input('Digite o nome do aluno 3: '))
d = (input('Digite o nome do aluno 4: '))

alunos=[a,b,c,d]

#The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
random.shuffle(alunos)
#reorganize the order of the list items
print(f'\033[31m {alunos}\033[m')