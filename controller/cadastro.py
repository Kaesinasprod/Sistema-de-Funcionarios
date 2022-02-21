import classes.funcionario_dao as func_dao
from qt_core import *
from classes.funcionario import Funcionario
from controller.mainwindow import *

class Cadastro(QWidget):
    def __init__(self, mainwindow, funcionario=None):
        super().__init__()
        uic.loadUi('view/cadastro.ui', self)
        self.cadastrar_btn.clicked.connect(self.salvar_funcionario)
        self.fechar_btn.clicked.connect(self.fechar_page)
        
        self.mainwindow = mainwindow
        self.funcionario = funcionario
        if funcionario != False:
            self.carrega_funcionario()

    def salvar_funcionario(self):
        nome = self.cad_nome.text()
        setor = self.cad_setor.text()
        cpf = self.cad_cpf.text()
        endereco = self.cad_end.text()
        #situacao = self.cad_situ.text()
        obs = self.cad_obs.text()
        #sexo = self.cad_sexo.text()
        #estado_civil = self.cad_civil.text()
        cep = self.cad_cep.text()
        telefone = self.cad_telefone.text()
        email = self.cad_email.text()
        salario = self.cad_salario.text()
        cargo = self.cad_cargo.text()
        escolaridade = self.cad_escolaridade.text()
        data_nascimento = self.cad_data.text()

        
        if self.funcionario != False: #edição
            funcionario_editado = Funcionario(self.funcionario.id, nome, setor, cpf, endereco, obs,
            cep, telefone, email, salario, cargo, escolaridade, data_nascimento)
            #INSERE NO BANCO DE DADOS
            func_dao.update_lista(funcionario_editado)


        else:
            #CRIA O OBJETO FUNCIONARIO
            novo_funcionario = Funcionario(None, nome, setor, cpf, endereco, obs,
            cep, telefone, email, salario, cargo, escolaridade, data_nascimento)
            #INSERE NO BANCO DE DADOS
            func_dao.insert(novo_funcionario)

        
        #REFERENCIA DO MAINWINDOW, CARREGA OS DADOS NO MAINWINDOW
        self.mainwindow.show_funcionarios_page()

    def fechar_page(self):
        self.mainwindow.show_funcionarios_page()


    def carrega_funcionario(self):
        self.cad_nome.setText(self.funcionario.nome)
        self.cad_setor.setText(self.funcionario.setor)
        self.cad_cpf.setText(self.funcionario.cpf)
        self.cad_end.setText(self.funcionario.end)
        #self.cad_situ.setText(self.funcionario.situ)
        self.cad_obs.setText(self.funcionario.obs)
        #self.cad_sexo.setText(self.funcionario.sexo)
        #self.cad_civil.setText(self.funcionario.estado_civil)
        self.cad_cep.setText(self.funcionario.cep)
        self.cad_telefone.setText(self.funcionario.telefone)
        self.cad_email.setText(self.funcionario.email)
        self.cad_salario.setText(self.funcionario.salario)
        self.cad_cargo.setText(self.funcionario.cargo)
        self.cad_escolaridade.setText(self.funcionario.escolaridade)
        self.cad_data.setText(self.funcionario.data_nascimento)


