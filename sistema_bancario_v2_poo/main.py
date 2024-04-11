import textwrap

from sistema_bancario_v2_poo.action.operacoes import criar_cliente, criar_conta, listar_contas, depositar, sacar, \
    exibir_extrato


def menu():
    menu = """\n
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tNovo usuário 
    [6]\tListar contas
    [0]\tSair  
    """
    return input(textwrap.dedent(menu))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\nOperação inválida")


main()
