def calculadora(opcao, primeiro_valor, segundo_valor):
    if opcao == '1':
        return primeiro_valor + segundo_valor
    elif opcao == '2':
        return primeiro_valor - segundo_valor
    elif opcao == '3':
        return primeiro_valor * segundo_valor
    elif opcao == '4':
        if segundo_valor == 0:
            return "Erro: Divisão por zero não é permitida."
        else:
            return primeiro_valor / segundo_valor


def main():
    while True:
        print("Bem vindo a minha calculadora!")
        print("Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("s: Sair")

        opcao = input("Digite o número para a operação que deseja: ")

        if opcao == 's':
            print("Saindo da calculadora...!")
            break
        elif opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe. Tente novamente.")
            continue

        try:
            primeiro_valor = float(input("Digite o primeiro valor: "))
            segundo_valor = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue

        resultado = calculadora(opcao, primeiro_valor, segundo_valor)
        print(f"\nO resultado é: {resultado:.2f}\n")


if __name__ == "__main__":
    main()
