from controller.lixeira import Lixeira
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
        self.novo_btn.clicked.connect(self.show_cadastro_page)
        #abre a lixeira
        self.lixeira.clicked.connect(self.show_lixeira)
        #abre a página inicial
        self.pesquisar_btn.clicked.connect(self.show_funcionarios_page)
        #barra de pesquisa
        self.pesquisa.textEdited.connect(self.text_edited)


        self.c = None



    def text_edited(self, txt_pesquisa):
        self.painel.insertWidget(0, FuncionariosPage(self, txt_pesquisa))
        self.painel.setCurrentIndex(0)


    def fechar_page(self):
        pass

    def show_funcionarios_page(self):
        self.painel.insertWidget(0, FuncionariosPage(self))
        self.painel.setCurrentIndex(0)

    def show_cadastro_page(self, funcionario=None):
        self.c = Cadastro(self, funcionario)
        self.c.show()

    def show_lixeira(self):
        self.painel.insertWidget(0, Lixeira(self))
        self.painel.setCurrentIndex(0)