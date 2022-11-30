'''
#Função lambda
  #É uma função (pequena) sem nome
  #Pode ter vários argumentos
  #Muito utilizado dentro de outras funções
  #Código mais 'clean'

#Ex:

somar10 = lambda x: x + 10
print(somar10(2))

#Lambda dentro de uma função

def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

print(somar(2))
'''