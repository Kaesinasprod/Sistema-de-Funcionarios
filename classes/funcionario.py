class Funcionario():
    def __init__(self, id, nome, setor, cpf, end, situ, obs, sexo, estado_civil, cep, telefone,
    email, salario, cargo, escolaridade, data_nascimento ,deletado=0):
        self.id = id
        self.nome = nome
        self.setor = setor
        self.cpf = cpf
        self.end = end
        self.situ = situ
        self.obs = obs
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.cep = cep
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.cargo = cargo
        self.escolaridade = escolaridade
        self.data_nascimento = data_nascimento
        self.deletado = deletado

    def getFunc(self):
        return [self.nome, self.setor, self.cpf, self.end, self.situ, self.obs, self.sexo, self.estado_civil, self.cep,
        self.telefone, self.email, self.salario, self.cargo, self.escolaridade, self.data_nascimento]