


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hackathon.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import webbrowser
from datetime import time

from PyQt5 import QtCore, QtGui, QtWidgets
from plyer import notification
from win10toast_click import ToastNotifier

from physic import Ui_SecondWindow


class Ui_MainWindow(object):
    def open_physicanalysis(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(70, 290, 161, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 290, 171, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda : self.open_physicanalysis())
        self.pushButton_3.setGeometry(QtCore.QRect(560, 290, 181, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 91, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 30, 241, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 90, 81, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 60, 81, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Notifications"))
        self.pushButton.clicked.connect(self.notify)
        self.pushButton_2.setText(_translate("MainWindow", "Mental Health"))
        self.pushButton_3.setText(_translate("MainWindow", "Physical Health"))
        self.label.setText(_translate("MainWindow", "NAME :"))
        self.label_2.setText(_translate("MainWindow", "AGE : "))
        self.label_3.setText(_translate("MainWindow", "Gender:"))

    def notify(self):
        c=0;
        toaster = ToastNotifier()
        while True:

            notification.notify(
                title="Water Break",
                message="PLEASE TAKE WATER",

                # displaying time
                timeout=2
            )
            # waiting time
            c=c+1
            time.sleep(120)
            if(c==2):
                toaster.show_toast("YOU CAN DO SOME EYE EXERCISE",duration=5,callback_on_click=webbrowser.open_new("https://www.youtube.com/watch?v=R5N8TA0KFxc"))

            notification.notify(
                title="SCREENTIME EXCEEDED",
                message="Please close your eyes for sometime you have exceeded the screen time limit.",

                # displaying time
                timeout=2
            )
            # waiting time
            time.sleep(3600)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

