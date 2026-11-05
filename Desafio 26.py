frase = input('Digite uma frase: ')
print(frase.title())
print(frase.count('a'))
print(frase.find('a'))
#indica a posição onde esta o caracteres 
P = frase
print(f'\033[35m{P.split()[1].count('a')}\033[m')
# split separa as palavra da frase com cada palavra sendo 0,1,2..