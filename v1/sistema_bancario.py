menu: str = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo: float = 0
limite: float = 500
extrato: str = ""
numero_saques: int = 0
LIMITE_SAQUES: int = 3


def depositar(valor: float, saldo: float) -> tuple[float, str]:
    novo_saldo = saldo + valor
    return novo_saldo, f"Depósito: R$ {valor:.2f}\n"


def sacar(valor: float, saldo: float, numero_saques_global: int) -> str | tuple[float, str]:
    if valor > saldo:
        return "Operação falhou! Você não tem saldo suficiente."
    elif valor > limite:
        return "Operação falhou! O valor do saque excede o limite."
    elif numero_saques_global >= LIMITE_SAQUES:
        return "Operação falhou! Número máximo de saques excedido."
    else:
        novo_saldo = saldo - valor
        return novo_saldo, f"Saque: R$ {valor:.2f}\n"


def exibir_extrato(saldo: float, extrato_global: str) -> None:
    if extrato_global:
        print("\n================ EXTRATO ================")
        print(extrato_global)
    else:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


while True:
    opcao: str = input(menu).lower()

    if opcao == "d":
        try:
            valor: float = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
            continue

        if valor > 0:
            saldo, operacao = depositar(valor, saldo)
            extrato += operacao
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        try:
            valor: float = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
            continue

        resultado_saque = sacar(valor, saldo, numero_saques)
        if isinstance(resultado_saque, str):
            print(resultado_saque)
        else:
            saldo, operacao = resultado_saque
            extrato += operacao

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
