from qt_core import *
from controller.card_func import CardFunc
import classes.funcionario_dao as func_dao

class FuncionariosPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/funcionarios_page.ui', self)

    def load(self):
        lista = func_dao.lista
        for c in lista:
            self.painel_func.addWidget(CardFunc(c))