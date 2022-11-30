'''

#List comprehension
#Mais simples de se escrever
#Utilizado quando você precisa criar uma nova lista a partir de uma existente.
#[expressão for iten in items]

#ex: Forma tradicional

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []

for item in frutas1:
  if 'n' in item:
    frutas2.append(item)

print(frutas2)

#ou

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

frutas2 = [item for item in frutas1 if 'n' in item]
print(frutas2)
'''
'''
#List comprehension com números
#Forma tradicional
valores = []

for x in range(6):
  valores.append(x * 10)

print(valores)

#ou

valores = [x * 10 for x in range(6)]
print(valores)
'''
'''
#lista e generator expression.
  #Uma forma mais rápida para listas, dicionários e etc
  #valores e bytes

#ex
from sys import getsizeof

numeros = [x * 10 for x in range(5)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print('-=' * 30)

numeros = (x * 10 for x in range(10))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))
'''