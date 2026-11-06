n1 = float(input('Primeira nota :'))
n2 = float(input('Segunda nota :'))
cores = {'amarelo':'\033[33m',
        'limpa' :'\033[m',
        'vermelho' :'\033[31m'}

s = (n1 + n2) / 2
print('A media é {}{:.1f}{}'.format(cores['amarelo'],s,cores['limpa']))
print(f'\033[32m Parabens \033[m 'if s>=6 else '\033[31m Estude Mais \033[m')