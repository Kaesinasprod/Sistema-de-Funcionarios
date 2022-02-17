from classes.funcionario import Funcionario
from qt_core import *
from icones.color import getColor
import classes.funcionario_dao as func_dao

class CardFunc(QWidget):
    def __init__(self, funcionario, mainWindow):
        super().__init__()
        uic.loadUi('view/card_func.ui', self)

        self.funcionario = funcionario
        self.mainWindow = mainWindow


        if len(funcionario.nome) > 0:
            self.icon.setText(funcionario.nome[0])
        self.nome.setText(funcionario.nome)
        self.prof.setText(funcionario.prof)
        self.cpf.setText(funcionario.cpf)
        self.end.setText(funcionario.end)
        #DETERMINA O ESTILO DA LABEL
        cor = getColor()
        style_sheet = f'border: 1px solid {cor}; border-radius: 25px; background-color: {cor};'
        self.icon.setStyleSheet(style_sheet)

        #Evento dos botões
        self.lixeira_btn.clicked.connect(self.remover)
        self.editar_btn.clicked.connect(self.mousePressEvent)

    def remover(self):
        if self.funcionario.deletado == 0: #VAI PARA LIXEIRA
            func_dao.update_lixeira(self.funcionario.id, deletado=1)
            self.mainWindow.show_funcionarios_page()
        else: #EXCLUI DEFINITIVAMENTE
            func_dao.delete(self.funcionario.id)
            self.mainWindow.show_lixeira()

    def mousePressEvent(self, event):
        self.mainWindow.show_cadastro_page(self.funcionario)