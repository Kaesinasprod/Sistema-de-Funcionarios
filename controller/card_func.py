from qt_core import *
from icones.color import getColor

class CardFunc(QWidget):
    def __init__(self, funcionario):
        super().__init__()
        uic.loadUi('view/card_func.ui', self)

        self.icon.setText(funcionario.nome[0])
        self.nome.setText(funcionario.nome)
        self.prof.setText(funcionario.prof)
        self.cpf.setText(funcionario.cpf)
        self.end.setText(funcionario.end)

        #DETERMINA O ESTILO DA LABEL
        cor = getColor()
        style_sheet = f'border: 1px solid {cor}; border-radius: 25px; background-color: {cor};'
        self.icon.setStyleSheet(style_sheet)