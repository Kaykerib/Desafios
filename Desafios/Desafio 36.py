print('====== Imobiliaria Feitosa ======')
valorcasa = int(input('Qual e o valor da casa que vais compra?'))
anos = int(input('Em quantos anos iria pagar a casa?'))
salario = int(input('Qual é o seu salario?'))

meses = anos * 12 
valoparcela = valorcasa / meses
v = salario * 0.30
print(meses)
if v > valoparcela:
  print(f'Pode compra a casa {valorcasa}')

else:
  print(f'Não pode compra a casa o seu empretimos foi negado!')






