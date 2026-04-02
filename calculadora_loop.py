continuar = "s"

while continuar == "s":
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = int(input("Digite a opção: "))
    if opcao == 1: 
        soma = numero1 + numero2 
        print(f'A soma é {soma}') 
    elif opcao == 2: 
        subtracao = numero1 - numero2
        print(f'A subtração é {subtracao}')
    elif opcao == 3:
        multiplicacao = numero1 * numero2
        print(f'A multiplicação é {multiplicacao}')    
    elif opcao == 4:
        if numero2 != 0:
            divisao = numero1 / numero2 
            print(f'A divisão é {divisao}')
        else:
            print('Não é possivel fazer essa divisão')

    else:   
        print('Numero inválido!')

    continuar = input("desejar continuar? (s/n)").lower()
