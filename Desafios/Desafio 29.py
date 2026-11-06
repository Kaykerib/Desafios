print('Velocidade maxima da via 80km')
v = int(input('Digite a velocidade do automovel: '))

##########

valorpaga= (v - 80) * 7

if v <= 80:
   print('\033[32m No limite \033[m')
else:
 

 print(f'Estar acima do limite, Voce iria paga 7$ cada kilimetro acima da velocida permitida! Valor a pagar por excesso de velocidade: \033[31m{valorpaga}\033[m $')
