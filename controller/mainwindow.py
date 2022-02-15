from qt_core import *
from controller.cadastro import Cadastro
from controller.funcionarios_page import FuncionariosPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/mainwindow.ui', self)
        # carrega a página inicial ao criar a janela
        self.show_funcionarios_page()
        #abre a página de cadastro
        self.Novo_btn.clicked.connect(self.show_cadastro_page)

    def fechar_page(self):
        pass

    def show_funcionarios_page(self):
        self.painel.insertWidget(0, FuncionariosPage(self))
        self.painel.setCurrentIndex(0)

    def show_cadastro_page(self, funcionario=None):
        self.painel.insertWidget(0, Cadastro(self, funcionario))
        self.painel.setCurrentIndex(0)

