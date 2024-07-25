import sys

from PyQt5.QtWidgets import QApplication, QWidget
from Ui_form import Ui_Form

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App Works')
window.setGeometry(100, 100, 500, 500)
gw = Ui_Form()
gw.setupUi(window)

window.show()
sys.exit(app.exec_())