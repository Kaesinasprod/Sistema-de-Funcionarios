import classes.funcionario_dao as func_dao
from qt_core import *
from classes.funcionario import Funcionario

class Cadastro(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/cadastro.ui', self)
        self.cadastrar_btn.clicked.connect(self.salvar_funcionario)
        self.cancelar_btn.clicked.connect(self.fechar_page)
        

    def salvar_funcionario(self):
        nome = self.cad_nome.text()
        prof = self.cad_prof.text()
        cpf = self.cad_cpf.text()
        endereco = self.cad_end.text()
        #CRIA O OBJETO FUNCIONARIOS
        novo = Funcionario(None, nome, prof, cpf, endereco)
        #INSERE NO BANCO DE DADOS
        func_dao.insert(novo)

    def fechar_page(self):
        self.hide()

