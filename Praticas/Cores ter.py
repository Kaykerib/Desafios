 ## STYLE          TEXT       BACK-FUNDO
# 0 none            30          40    BRANCO      
# 1 Bold            31          41    VERMELHO
#_4 UnderlinE       32          42    VERDE
#7 Negative         33          43    AMARELHO
#                   34          44    AZUL
#                   35          45    ROXO
#                   36          46    AZUL MARINHO
#                   37          47    CINZA
#  
#print('\033[4;30;45mOla, mundo!\033[m')
print('\033[7;30m Ola, mundo!\033[m')
a = 3 
b = 4
cores ={'limpa' :'\033[m',
        'azul' :'\033[34m',
        'amarelo' :'\033[33m',
        'pretoebranco' :'\033[7;30m',
        'vermelho' :'\033[31m',
        'roxo':'\033[35m',
        'azul marinho' :'\033[36m',
        'cinza' :'\033[37m',
        'branco' :'\033[30m',
        'verde' :'\033[32m'}


print(f'os valores são \033[32m{a}\033 e \033[31m{b} \033')

print('ola! muito preazer,{}{}{}'.format('\033[4;43m', a , '\033[m'))

print('ola! muito preazer,{}{}{}'.format(cores['pretoebranco'], b, cores['limpa']))