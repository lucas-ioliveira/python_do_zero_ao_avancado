'''
#Função Map em uma lista
  #Muito utilizado com listas
  #Aplicar uma função a um Iterable, por item.(list,tuple,dic,etc.)

#ex:
lista1 = [1,2,3,4]

def mult(x):
  return x * 2

print(mult(2))

lista2 = map(mult, lista1)#map vai associar a função a lista

print(list(lista2))#list converte o resultado para exibir em lista.

#Função Map com lambda

lista1 = [1,2,3,4]

lista2 = map(lambda x: x * 2, lista1)

print(list(lista2))
'''