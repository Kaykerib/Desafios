from datetime import date
print('»»»»»»»» Serviço Militar »»»»»»»»')
datahoje = date.today().year
print(datahoje)
nascimento = int(input('Qual é a sua data de nascimento?'))
idade = datahoje - nascimento


if idade < 18:
    saldo = 18 - idade
    print('tens tempo ainda antes de alista no Serviço')
    ano = datahoje + saldo
    print(f'Vc ainda tem {saldo} para ser alista ainda')
elif idade > 18:
 saldo = idade - 18
 print('Já passou a hora de entra no Serviço')
 ano = datahoje - saldo
 print(f'ja passou {saldo}')
else:
   print('Esta na hora de entra no Sevriço')   