c = input('Digite o nome de uma Cidade: ')
print(c.title())

print(False if c.find('Santo') is -1 else True)
# Verifica se a palavra "Santo" existe no texto.
# Se não encontrar, retorna False; 'else'caso contrário, retorna True.
