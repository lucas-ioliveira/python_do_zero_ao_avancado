'''
#Set (Listas)
  #Similar a listas
  #Evita itens duplicados
  #Não utiliza index
#Ex

list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # uniom (união)
print(num1 - num2) #Difference
print(num1 ^ num2) #Symmetric Difference
print(num1 & num2) # And
'''
'''
#Funções em sets

s1 = {1,2,3,4,5,6}
s1.add(7) #Adiciona um item ao final
s1.update({7,8,9,10}) #Adiciona vários itens
s1.remove(10) #Remove
print(s1)
'''
'''
#Sets com string

set1 = {'a', 'b', 'c',}
set2 = {'a','d','e'}
set3 = {'c','d','f'}

set4 = set1.union(set3)
print(set4)
'''