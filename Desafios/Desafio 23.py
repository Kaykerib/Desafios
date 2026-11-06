num = int(input('Digite um numero'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10 
m = num // 1000 % 10 

cores = {
        'endtag' : '\033[m',
        'azul' :'\033[34m',
        'amarelo' :'\033[33m',
        'pretoebranco' :'\033[7;30m',
        'vermelho' :'\033[31m',
        'roxo':'\033[35m',
        'azul marinho' :'\033[36m',
        'cinza' :'\033[37m',
        'branco' :'\033[30m',
        'verde' :'\033[32m'}
 

 

print('Analisando o número {}{]{}'.fomrat(cores['amarelo'],num,cores['endtag']))
print('Unidade {}{}{}'.fomrat(cores['azul'],u, cores['endtag']))
print('Dezena {}{}{}'.fomrat(cores['azul marinho'],d,cores['endtag']))
print('Centena {}{}{}'.fomrat(cores['cinza'],c,cores['endtag']))
print('Milhar {}{}{}'.fomrat(cores['pretoebranco'],m,cores['endtag']))




