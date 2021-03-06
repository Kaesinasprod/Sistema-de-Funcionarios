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

        #GROUPBOX
        situ = 'Trabalhando' if self.rb_situacao.isChecked() == True else 'Afastado'
        sexo = 'Masculino' if self.rb_sexo.isChecked() == True else 'Feminino'
        estado_civil = 'Solteiro' if self.rb_civil.isChecked() == True else 'Casado'

        obs = self.cad_obs.text()
        cep = self.cad_cep.text()
        telefone = self.cad_telefone.text()
        email = self.cad_email.text()
        salario = self.cad_salario.text()
        cargo = self.cad_cargo.text()
        escolaridade = self.cad_escolaridade.text()
        data_nascimento = self.cad_data.text()
        self.close()

        
        if self.funcionario != False: #edição
            funcionario_editado = Funcionario(self.funcionario.id, nome, setor, cpf, endereco, obs,
            cep, telefone, email, salario, cargo, escolaridade, data_nascimento, situ, sexo,
            estado_civil)
            #INSERE NO BANCO DE DADOS
            func_dao.update_lista(funcionario_editado)


        else:
            #CRIA O OBJETO FUNCIONARIO
            novo_funcionario = Funcionario(None, nome, setor, cpf, endereco, obs,
            cep, telefone, email, salario, cargo, escolaridade, data_nascimento, sexo, estado_civil, situ)
            #INSERE NO BANCO DE DADOS
            func_dao.insert(novo_funcionario)

        
        #REFERENCIA DO MAINWINDOW, CARREGA OS DADOS NO MAINWINDOW
        self.mainwindow.show_funcionarios_page()

    def fechar_page(self):
        self.close()


    def carrega_funcionario(self):
        self.cad_nome.setText(self.funcionario.nome)
        self.cad_setor.setText(self.funcionario.setor)
        self.cad_cpf.setText(self.funcionario.cpf)
        self.cad_end.setText(self.funcionario.end)
        self.cad_obs.setText(self.funcionario.obs)

        self.situ_trabalhando.setChecked(True if self.funcionario.situ == 'Trabalhando' else False)
        self.situ_afastado.setChecked(True if self.funcionario.situ == 'Afastado' else False)

        self.sexo_masculino.setChecked(True if self.funcionario.sexo == 'Masculino' else False)
        self.sexo_feminino.setChecked(True if self.funcionario.sexo == 'Feminino' else False)

        self.estado_civil_solteiro.setChecked(True if self.funcionario.estado_civil == 'Solteiro' else False)
        self.estado_civil_casado.setChecked(True if self.funcionario.estado_civil == 'Casado' else False)

        self.cad_cep.setText(self.funcionario.cep)
        self.cad_telefone.setText(self.funcionario.telefone)
        self.cad_email.setText(self.funcionario.email)
        self.cad_salario.setText(self.funcionario.salario)
        self.cad_cargo.setText(self.funcionario.cargo)
        self.cad_escolaridade.setText(self.funcionario.escolaridade)
        self.cad_data.setText(self.funcionario.data_nascimento)


