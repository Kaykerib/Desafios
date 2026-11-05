nome =str(input('Digite um nome'))

if nome == 'Gustavo':
    print('Que nome bunito')
elif nome == 'Pedro' or nome == 'Maria' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
        print('Belo nome feminino')
else: 
     print('Seu nome é bem normal.')
print('Tenha um bom dia,{}'.formar(nome)) 


for valor in range(10):
 valor = int(input('Valor da compra: '))
 if valor > 0 or valor < 1001:
  break