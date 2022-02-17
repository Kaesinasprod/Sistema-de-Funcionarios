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
        prof = self.cad_prof.text()
        cpf = self.cad_cpf.text()
        endereco = self.cad_end.text()
        
        if self.funcionario != False: #edição
            funcionario_editado = Funcionario(self.funcionario.id, nome, prof, cpf, endereco)
            #INSERE NO BANCO DE DADOS
            func_dao.update_lista(funcionario_editado)


        else:
            #CRIA O OBJETO FUNCIONARIO
            novo_funcionario = Funcionario(None, nome, prof, cpf, endereco)
            #INSERE NO BANCO DE DADOS
            func_dao.insert(novo_funcionario)

        
        #REFERENCIA DO MAINWINDOW, CARREGA OS DADOS NO MAINWINDOW
        self.mainwindow.show_funcionarios_page()

    def fechar_page(self):
        self.mainwindow.show_funcionarios_page()


    def carrega_funcionario(self):
        self.cad_nome.setText(self.funcionario.nome)
        self.cad_prof.setText(self.funcionario.prof)
        self.cad_cpf.setText(self.funcionario.cpf)
        self.cad_end.setText(self.funcionario.end)


