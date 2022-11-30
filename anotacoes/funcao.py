'''
#Função
Ex:1

def boas_vinda():
  nome = str(input('Digite seu nome: '))
  print(f'Olá, {nome}!')
  print('Temos 5 notebooks em estoque!')

boas_vinda()


#ex 2

def somar_dois_numeros():
  numero1 = 10
  numero2 = 5
  resultado = numero1 + numero2
  print(resultado)

somar_dois_numeros()


#ex3 - Parâmetros e argumentos

def boas_vindas(nome, quantidade): #Entre esses () são os parâmetros.
  print(f'Olá, {nome}.')
  print(f'Temos {str(quantidade)} nootboks em estoque')

boas_vindas('Marcos', 5) #Entre esses () são os argumentos.


#ex3 - Argumentos default e non-default
# o argumento que será definido sempre será o ultimo.

#ex4 - print ou retur em função

def cliente1(nome):
  print(f'olá, {nome}') # É uma tarefa e não armazena nada.

cliente1('maria')

def cliente2(nome):
  return f'Olá, {nome}' # Pode ser armazenado e ultilizado depois.

cliente2('José')
'''

#Vários argumentos xargs com números.

#ex
'''
def soma(*numeros):
  return numeros

x = soma(2,3,4,7)
print(x)


#Vários argumentos e parâmetros xargs com números.
#O retorno é um dicionário.

#ex

def agencia_carros(**carros):
  return carros

print(agencia_carros(marca='gol', cor='Branco', motor=1.0, placa=123456))
print(agencia_carros(marca='gol', cor='preto', motor=1.6, placa=654321))
'''