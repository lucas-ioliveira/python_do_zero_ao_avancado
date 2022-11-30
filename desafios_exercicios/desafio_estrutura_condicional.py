# Temperatura if,elif,else

try:
  print('--App temperatura--')
  temperatura = int(input("Qual a temperatura da carne: "))

#Condições
  if temperatura < 48:
    print('Seu steak está cru! favor, assar por mais alguns minutos.')

  elif temperatura == 48 or temperatura < 54 :
    print('Seu steak está selada.')

  elif temperatura == 54 or temperatura < 60:
    print('Seu steak está ao ponto para mal')

  elif temperatura == 60 or temperatura < 65:
    print('Seu steak está ao ponto')

  elif temperatura == 65 or temperatura < 71:
    print('Seu steak está ao ponto para bem')

  elif temperatura == 71 or temperatura < 80:
    print('Seu steak está bem passado')

  elif temperatura >= 81:
    print('Seu steak está queimado')

except:
  print('Digite um valor válido.')
