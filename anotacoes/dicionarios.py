'''
#Introdução a dicionários

#Dicionários
  #Utiliza index no formato de keys(chave) e values(valor)
  #Aceita string, inteiros, float, boolean...

aluno = {'nome': 'Lucas', 'idade': 25, }
print(aluno)

#Atualizando itens no dicionário
aluno['nome'] = 'Isaias' #Somente 1 item
print(aluno)

aluno.update({'nome':'Oliveira', 'idade': 20}) #Vários itens.
print(aluno)

del aluno['idade']
print(aluno)


#Looping dentro de um dicionário
aluno = {'nome': 'Lucas', 'idade': 25, 'nota_final': 'A', 'aprovação':True }
print(aluno)

for x in aluno.items(): #O retorno vem em tuplas.
  print(x)

for keys, values in aluno.items(): #O retorno vem fora de tuplas
  print(keys, values)
'''