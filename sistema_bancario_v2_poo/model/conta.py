from model.historico_cliente import HistoricoCliente


class Conta:
    def __init__(self, numero_conta, cliente):
        self._numero_conta = numero_conta
        self._saldo = 0
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = HistoricoCliente()

    @property
    def historico(self):
        return self._historico
    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente.")
            return False

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso.")

        else:
            print("Operação falhou, valor informado é inválido.")
            return False

    def depositar(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso.")
            return True
        else:
            print("Valor informado é inválido.")
            return False
