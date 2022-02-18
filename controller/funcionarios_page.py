from controller.card_func import CardFunc
from qt_core import *
import classes.funcionario_dao as func_dao

class FuncionariosPage(QWidget):
    def __init__(self, mainWindow,txt_pesquisa=''):
        super().__init__()
        uic.loadUi('view/funcionarios_page.ui', self)
        
        self.mainWindow = mainWindow
        self.txt_pesquisa = txt_pesquisa
        
        self.load()

    def load(self):
        lista = func_dao.selectAll(self.txt_pesquisa)
        for funcionario in lista:
            self.painel_func.addWidget(
                CardFunc(funcionario, self.mainWindow))