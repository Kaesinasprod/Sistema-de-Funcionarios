class Funcionario():
    def __init__(self, id, nome, prof, cpf, end, deletado=0):
        self.id = id
        self.nome = nome
        self.prof = prof
        self.cpf = cpf
        self.end = end
        self.deletado = deletado

    def getFunc(self):
        return [self.nome, self.prof, self.cpf, self.end]