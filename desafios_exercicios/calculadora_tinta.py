# Funções para os calculos
def calculo_tinta():
    area = altura * largura
    resultado = area / rendimento
    print(f'você necessita de {resultado} latas de tinta.')


while True:
    try:
        print()
        print('--App Calculadora para tinta--')
        print('Se desejar sair digite: "00"')

        # Interação com o usuário
        rendimento = int(input('Qual o rendimento da lata de tinta: '))

        # condição para encerrar o programa
        if rendimento == 00:
            print('Encerrando o programa, até a próxima.')
            break

        # Interação com o usuário
        altura = int(input('Qual a altura da parede: '))
        largura = int(input('Qual a largura da parede: '))

        print()

        # Calculo
        calculo_tinta()

    except:
        print('Digite uma opção válida.')
