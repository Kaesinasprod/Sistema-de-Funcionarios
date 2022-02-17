from qt_core import *
from controller.mainwindow import *
import classes.funcionario_dao as func_dao
from controller.card_func import CardFunc


class Lixeira(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/lixeira.ui', self)

        self.mainWindow = mainWindow
        self.load()

        #EVENTO DOS BOTÕES
        self.fechar_btn.clicked.connect(self.fechar_page)

    def fechar_page(self):
        self.mainWindow.show_funcionarios_page()

    def load(self):
        lista = func_dao.selectLixeira()
        for funcionario in lista:
            self.painel_func.addWidget(
                CardFunc(funcionario, self.mainWindow))
        