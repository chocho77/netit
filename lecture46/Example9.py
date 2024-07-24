import sys
#from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton as qt
#import PyQt6.QtWidgets as qt
from PyQt5 import QtWidgets as qt

class MainWindow(qt.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        button = qt.QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")


app = qt.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()