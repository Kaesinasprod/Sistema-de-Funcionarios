from qt_core import *
from controller.login import *


app = QApplication(sys.argv)
win = Login()
win.show()
sys.exit(app.exec())