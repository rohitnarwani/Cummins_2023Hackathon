# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import main


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.Mainwin()
        # showing all the widgets
        self.show()



    def Mainwin(self):
     layout = QGridLayout()
     layout.addWidget(QPushButton("Mental Analysis"), 1, 0)
     layout.addWidget(QPushButton("Physical Analysis"), 1, 1)

     self.setLayout(layout)




App = QApplication(sys.argv)


window = Window()


sys.exit(App.exec())
notification.notify(
                title="SCREENTIME EXCEEDED",
                message="Please close your eyes for sometime you have exceeded the screen time limit.",

                # displaying time
                timeout=2
            )