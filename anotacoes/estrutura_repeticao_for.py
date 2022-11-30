'''
#For loops

for numero in range(1, 6):
  print(numero)
'''
'''
#For loops - utilizando srings

palavra = 'Google'
for letra in palavra:
  print(letra)

palavra1 = 'Espetacular'
for letra1 in palavra1:
  print(f'{letra1} está dentro da palavra {palavra1}')
'''

# For loops - utilizando if e else
'''
compra_confirmada = True
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada.'

for enviar in range(3):
    if compra_confirmada:
      print(dados_compra)
      print('Detalhes enviado para seu e-mail.')
      break

    else:
      print('Falha na compra')  
'''
'''
# for loop nested
  #Outer loop
    #Inner loop

for numero1 in range(1, 6):
  print('Produto' + str(numero1))
  for numero2 in range(11):
    print(numero1, numero2)
'''
'''
# for loop Separando Strings

#Modificar de FANTASTICO para F A N T A S T I C O
palavra = 'FANTASTICO '
for espaco in palavra:
  print(f'{espaco}', end=' ')
'''