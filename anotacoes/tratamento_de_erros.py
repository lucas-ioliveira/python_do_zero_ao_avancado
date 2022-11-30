'''
#Erros
  #são excelentes para testes
  #não realiza o 'stop' no programa
  #mensagens customizadas quando encontra um erro
  #Try é uma tentativa
  #Except é a excessão da tentativa, consigo imprimir uma menssagem personalizada do erro.

#ex

try:
  letras = ['a', 'b', 'c']
  print(letras[3])
except IndexError:
  print('O index não existe.')

#Trabalhando com try e except com input
#ex:

try:
  valor = int(input('Digite o valor do seu produto: R$'))
  print(valor)
except ValueError:
  print('Favor, digitar um valor em números')

#Adicionando o else e finally
#ex:
try:
  valor = int(input('Digite o valor do seu produto: R$'))
  print(valor)
except ValueError:
  print('Favor, digitar um valor em números')
else:
  print('Usuário digitou um valor correto')
  resultado = valor * 2
  print(resultado)

#obs: caso seja necessário continuar o bloco de código mesmo com o erro usar o finally no lugar do else

try:
  valor = int(input('Digite o valor do seu produto: R$'))
  print(valor)
except ValueError:
  print('Favor, digitar um valor em números')
finally:
  print('Código ok')
'''