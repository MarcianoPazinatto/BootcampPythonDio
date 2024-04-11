from sistema_bancario_v2_poo.model.conta import Conta
from sistema_bancario_v2_poo.action.saque import Saque


class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def saques(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
             if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print("\nLimite de saque excedido")

        elif excedeu_saques:
            print("numero máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
                Agência: \t {self._agencia}
                C/C: \t\t {self._numero_conta}
                Titular: \t {self._cliente.nome}           
                """
