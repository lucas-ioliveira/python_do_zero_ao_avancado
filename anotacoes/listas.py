'''
#Sobre listas#

#ex
estados = ['Pará', 'Rio de janeiro', 'Ceará', 'São Paulo']
print(estados)

#Manipulando listas
#numeros = [2, 4, 6]
print(estados[1])

#Substituir item

estados[2] = 'Brasília'
print(estados)

#Funções dentro de listas
estados = ['Pará', 'Rio de janeiro', 'Ceará', 'São Paulo']

#Adicionando item ao final da lista
estados.append('Brasília')
print(estados)

#Removendo item
estados.remove('Pará')

#Concatenando listas

numeros = [2, 3, 4, 5]
letras = ['a' ,'b', 'c', 'd']

#final = numeros * 2
final = numeros + letras
#ou pode ser usado uma função para a mesma finalidade.
numeros.extend(letras)
print(numeros)

#Listas dentro de listas
itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[1])

#Repetição em uma lista

valores = [50, 80, 110, 150,170]
for x in valores:
  print(f'O valor final dp produto é de R${x}')

#Verificando itens em uma lista
cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
  print('Em estoque.')
else:
  print('Não temos essa cor em estoque.')

#Agregando duas listas com o zip
cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)
print(list(duas_listas))

#input em uma lista
frutas_usuario = input('Favor, digitar o nome das frutas separados por virgulas.')

frutas_lista = frutas_usuario.split(', ')
print(frutas_usuario)
'''