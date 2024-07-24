import sys
from PyQt5 import QtWidgets 
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(QtWidgets.QWidget):
  def __init__(self, *args, **kwargs):
    super().__init__()
    # ------------------------ your code start here --------------------------

    # ------------------------- your code ends here --------------------------
    self.show()

  # -------------------------- create your methods here ----------------------



if __name__ == '__main__':
  
  app = QtWidgets.QApplication(sys.argv)

  window = MainWindow()

  sys.exit(app.exec_)

  

  

