from qt_core import *
from controller.cadastro import Cadastro
from controller.funcionarios_page import FuncionariosPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/mainwindow.ui', self)
        self.Novo.triggered.connect(self.salvar_funcionario)
        
        #INSERE NA PÁGINA INICIAL
        self.show_funcionarios_page

    def salvar_funcionario(self):
        self.win = Cadastro()
        self.win.show()

    def fechar_page(self):
        pass

    def show_funcionarios_page(self):
        self.painel.insertWidget(0, FuncionariosPage())
        self.painel.setCurrentIndex(0)

    def show_cadastro_page(self):
        self.painel.insertWidget(1, Cadastro())
        self.painel.setCurrentIndex(1)

