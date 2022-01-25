from qt_core import *

class CardFunc(QWidget):
    def __init__(self, funcionario):
        super().__init__()
        uic.loadUi('view/card_func.ui', self)

        self.icon.setText(funcionario.nome[0])
        self.nome.setText(funcionario.nome)