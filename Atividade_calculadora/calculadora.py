print("Seja bem vindo a calculadora ijj")
print("-------------------------------")

while True:
    print("Você pode escolher entre as seguintes operações:")
    print("- Soma (+)")
    print("- Subtração (-)")
    print("- Multiplicação (*)")
    print("- Divisão (/)")
    print("- Potência (**)")

    operacao = input("Qual operação deseja fazer:" ) 
    numero1 = float (input("Informe o primeiro numero: "))
    numero2 = float (input("Informe o segundo numero: "))

    match operacao:

        case '+':
            print(f"{numero1} + {numero2} = {(numero1 +  numero2)}")
        case '-':
            print(f"{numero1} - {numero2} = {(numero1 - numero2)}")
        case '*':
            print(f"{numero1} * {numero2} = {(numero1 * numero2)}")
        case '/':
            print(f"{numero1} / {numero2} = {(numero1 / numero2)}")
        case '**':
            print(f"{numero1} ** {numero2} = {(numero1 ** numero2)}")
        case _:
            print("Operação inválida!")
            
    sair = input("Deseja continuar? s ou n ")

    if sair == 'n':
        break