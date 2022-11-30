'''
#Função Filter
  #Muito utilizado com listas
  #Aplicar uma função a um iterble, filtrando os items. (list,tuple,dic e etc.)

#ex:

valores = [10,12,34,44,57]

def remover20(x):
  return x > 20

print(list(filter(remover20, valores)))

#OU

print(list(filter(lambda x: x > 20, valores)))
'''