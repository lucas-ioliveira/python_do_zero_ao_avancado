#Importação da biblioteca sleep
from time import sleep
#Laço de repetição
while True:
  print()
  print('App calculadora')

  mensagem = '''
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    [0] - Sair
  '''
  print(mensagem)
  #Interação com o usuário.
  opcao = int(input('Escolha uma opção: '))
  #Condição para finalizar o programa.
  if opcao == 0:
    print('App finalizado.')
    break
  #Interação com o usuário.
  n1 = int(input('Digite um número: '))
  n2 = int(input('Digite outro número: '))

  #Funções com os calculos matemáticos.
  def somar():
    resultado = n1 + n2
    print(resultado)

  def subtrair():
    resultado = n1 - n2
    print(resultado)

  def multiplicar():
    resultado = n1 * n2
    print(resultado)

  def dividir():
    resultado = n1 / n2
    print(resultado)

  #Condições.
  if opcao == 1:
    print('Calculando..')
    sleep(2)
    print('O seu resultado é:')
    somar()

  elif opcao == 2:
    print('Calculando..')
    sleep(2)
    print('O seu resultado é:')
    subtrair()

  elif opcao == 3:
    print('Calculando..')
    sleep(2)
    print('O seu resultado é:')
    multiplicar()

  elif opcao == 4:
    print('Calculando..')
    sleep(2)
    print('O seu resultado é:')
    dividir()

  else:
    print('Digite uma opção válida.')
