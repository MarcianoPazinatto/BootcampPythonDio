from model.cliente import Cliente


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_de_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
