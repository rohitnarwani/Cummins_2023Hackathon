# Form implementation generated from reading ui file 'testmental.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = QtWidgets.QWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(120, 90, 591, 391))
        self.graph.setObjectName("graph")

        self.label_2 = QtWidgets.QLabel(self.graph)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 111, 41))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.graph)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 41))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.graph)
        self.lineEdit.setGeometry(QtCore.QRect(200, 29, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.graph)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.graph)
        self.label_3.setGeometry(QtCore.QRect(100, 200, 300, 41))
        self.label_3.setObjectName("label_3")


        self.label_6 = QtWidgets.QLabel(self.graph)
        self.label_6.setGeometry(QtCore.QRect(300, 300, 300, 41))
        self.label_6.setPixmap(QPixmap('img.jpg'))

        self.pushButton = QtWidgets.QPushButton(self.graph,clicked=lambda:self.onclick())
        self.pushButton.setGeometry(QtCore.QRect(140, 150, 101, 31))
        self.pushButton.setObjectName("pushButton")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def onclick(self):
        height=self.lineEdit.text()
        weight=self.lineEdit_2.text()
        bmi_value=int(weight)/(int(height)*int(height))
        if ( bmi_value > 0):
            if ( bmi_value <= 16):

                self.label_3.setText('yor BMI Index is:' + str(bmi_value)+'Your are very underweight')
            elif ( bmi_value <= 18.5):
                self.label_3.setText('yor BMI Index is:' + str(bmi_value) + 'Your are  underweight')
            elif ( bmi_value<= 25):

                self.label_3.setText('yor BMI Index is:' + str(bmi_value) + 'Congrats! You are Healthy')
            elif ( bmi_value <= 30):
                self.label_3.setText('yor BMI Index is:' + str(bmi_value) + 'Your are  overweight')
            else:
                self.label_3.setText('yor BMI Index is:' + str(bmi_value) + 'Your are very overweight')
        else:
            self.label_3.setText('enter valid details')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Weight:"))
        self.label.setText(_translate("MainWindow", "Height:"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "submit"))

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())