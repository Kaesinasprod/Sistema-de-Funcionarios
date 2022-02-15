from qt_core import *
from controller.mainwindow import MainWindow

class Login(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/login.ui', self)
        self.entrar_btn.clicked.connect(self.login)
        self.win = None
    

    def login(self):
        usuario = 'admin'
        senha = 'admin'
        user = self.usuario.text()
        password = self.senha.text()
        if usuario == user and password == senha:
            self.win = MainWindow()
            self.win.show()
            self.hide()
        else:
            print("Erro")