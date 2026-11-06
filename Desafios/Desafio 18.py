import math
angulo = float(input('digite o angulo'))
seno= math.sin(math.radians(angulo))
co= math.cos(math.radians(angulo))
tan= math.tan(math.radians(angulo))

def colorir (text, cor):
 cores = { 
        'azul' :'\033[34m',
        'amarelo' :'\033[33m',
        'pretoebranco' :'\033[7;30m',
        'vermelho' :'\033[31m',
        'roxo':'\033[35m',
        'azul marinho' :'\033[36m',
        'cinza' :'\033[37m',
        'branco' :'\033[30m',
        'verde' :'\033[32m'
 } 
 endtag = '\033[m'

 return f"{cores[cor]}{text}{endtag}"

print(f"O angulo {colorir(angulo,'azul marinho')} tem o Seno    {colorir(f'{seno:.2f}','cinza')} e o Cosseno {colorir(f'{co:.2f}','branco')} é Tangente {colorir(f'{tan:.2f}', 'verde')} desse Ângulo")