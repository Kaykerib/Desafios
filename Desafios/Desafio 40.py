print("===== Media final =====")
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

cores ={'endtag' :'\033[m',
        'azul' :'\033[34m',
        'amarelo' :'\033[33m',
        'pretoebranco' :'\033[7;30m',
        'vermelho' :'\033[31m',
        'roxo':'\033[35m',
        'azul marinho' :'\033[36m',
        'cinza' :'\033[37m',
        'branco' :'\033[30m',
        'verde' :'\033[32m'}

media = (nota1 + nota2) / 2

if media > 7:
     print(f' \033[32m Aprovado \033[m media {media}')
    
elif media >= 5 and 6.9:
    print(f'\033[33m Recuperação \033[m media {media}')
else:
    print(f'\033[31m Reprovado \033[m media {media}')
   
    