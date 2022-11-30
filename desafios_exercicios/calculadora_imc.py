# Calculo de IMC#

# Qual a altura em cm:
# Qual é o seu peso em kg:

# Menor que 18,5 Magreza;
# Entre que 18,5 e 24,9 Normal;
# Entre que 25,0 e 29,9 Sobrepeso;
# Entre que 30,0  e 39,9 Obesidade;
# Maior que 40,0 Obesidade grave;

# Laço de repetição
while True:
    try:

        print()
        print('--App calculadora IMC--')
        print('''
            [1] - Calcular
            [00] - Encerrar
    ''')

        print()

        # Interação com o usuário para saber a opção desejada.
        opcao = int(input('Digite a opção desejada: '))
        # Condição para o programa encerrar
        if opcao == 00:
            print('Programa encerrado, até a próxima.')
            break

            # Interação com o usuário
        altura = float(input('Digite a altura: '))
        peso = float(input('Digite o peso: '))


        def calculo_imc():
            imc = peso / (altura ** 2)
            print(f'Seu imc é {imc:.2f}.')
            return imc


        calculo_imc = calculo_imc()
        print()

        # Condições para saber o status do imc
        if opcao == 1:
            if calculo_imc < 18.5:
                print('Magreza.')

            elif calculo_imc >= 18.5 and calculo_imc < 24.9:
                print('Normal.')

            elif calculo_imc >= 25 and calculo_imc < 29.9:
                print('Sobrepeso.')

            elif calculo_imc >= 30 and calculo_imc < 39.9:
                print('Obesidade.')

            elif calculo_imc > 40:
                print('Obesidade Grave.')

            else:
                print('Morte em breve')

    except:
        print('Digite um valor válido.')
