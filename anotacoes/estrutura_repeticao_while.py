#While loops
'''
-Excelentes para loops dependentes de uma condição.
-Criar uma promoção para um produto no valor de R$100.

valor = 100
dia = 0

while valor > 20:
  dia +=1
  print(f' No dia {dia} o produto será vendido por R${valor}')
  valor -= 5
'''
'''
Publicar um produto com comissão de 10% se for acima de R$20,00


valor = input('Digite o valor do seu produto: ')
valor = int(valor)

while valor > 20:
  valor = (valor * 0.10) + valor
  print(f'O valor final do seu produto será de R${valor:.2f}')
  break
'''