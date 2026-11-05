n = int(input('Digite um numero:'))
a = 2
g = 3
cores ={'limpa' :'\033[m',
        'VERDE' :'\033[32m',
        'AZUL' :'\033[34m',
        'pretoebranco' :'\033[7;30m',}
d = n * a
t = n * g
r = n ** (1/2)
print('O dobro de {}{}{} e o triplo é {}{}{} é raiz quadrada {}{:.2f}{}'.format(
  cores['AZUL'],d, cores['limpa'],
  cores['VERDE'],t, cores['limpa'],
  cores['pretoebranco'],r, cores['limpa']
  ))