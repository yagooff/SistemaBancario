menu = """
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 0
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo += valor_deposito
        extrato += f"Depósito: +R${valor_deposito}\n"

    elif opcao == "s":
        if numero_de_saques < LIMITE_DE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: "))
            if saldo >= valor_saque:
                saldo -= valor_saque
                extrato += f"Saque: -R${valor_saque}\n"
                numero_de_saques += 1
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques excedido.")

    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R${saldo}")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
