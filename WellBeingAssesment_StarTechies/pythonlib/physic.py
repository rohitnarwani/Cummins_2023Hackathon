


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(877, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = QtWidgets.QWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(30, 30, 1500, 800))
        self.graph.setObjectName("graph")
        self.label_2 = QtWidgets.QLabel(self.graph)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 41))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.graph)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.graph)
        self.lineEdit.setGeometry(QtCore.QRect(260, 20, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.graph)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 80, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.graph)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 291, 31))
        self.label_3.setObjectName("label_3")

        '''self.label_6 = QtWidgets.QLabel(self.graph)
        self.label_6.setGeometry(QtCore.QRect(300, 300, 500, 500))
        self.label_6.setPixmap(QPixmap('img.jpg'))'''

        self.pushButton = QtWidgets.QPushButton(self.graph,clicked=lambda: self.onclick())
        self.pushButton.setGeometry(QtCore.QRect(260, 150, 100, 60))
        self.pushButton.setObjectName("pushButton")

        #self.pushButton = QtWidgets.QPushButton(self.graph, clicked=lambda: self.onclick())

        self.label_4 = QtWidgets.QLabel(self.graph)
        self.label_4.setGeometry(QtCore.QRect(420, 30, 400, 250))

        self.label_4.setObjectName("label_4")
        self.label_4.setPixmap(QPixmap('phyimg.jpg'))

        self.DietPlan = QtWidgets.QLabel(self.graph)
        self.DietPlan.setGeometry(QtCore.QRect(10, 290,1500,500))
        self.DietPlan.setObjectName("")
        ##self.DietPlan.setPixmap(QPixmap('imgjpg'))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 21))
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
        self.label_2.setText(_translate("MainWindow", "Enter Your Weigt(KG):"))
        self.label.setText(_translate("MainWindow", "Enter Your Height In(CM)"))
        self.label_3.setText(_translate("MainWindow", "CONCLUSION:"))
        self.pushButton.setText(_translate("MainWindow", "submit"))
        #self.label_4.setText(_translate("MainWindow", "img"))
        self.DietPlan.setText(_translate("MainWindow", "DIET PLAN"))

    def onclick(self):
        height = self.lineEdit.text()
        weight = self.lineEdit_2.text()
        bmi_value = int(weight) / (int(height) * int(height))
        if (bmi_value > 0):
            if (bmi_value <= 16):

                self.label_3.setText('yor BMI Index is:' + str(bmi_value) + '.....Your are  underweight')
                self.DietPlan.setPixmap(QPixmap('gainwDietPlan.jpeg'))


            elif (bmi_value <= 25):

                self.label_3.setText('yor BMI Index is:' + str(bmi_value) + '.....Congrats! You are Healthy')
            elif (bmi_value <= 30):
                self.label_3.setText('yor BMI Index is:' + str(bmi_value) + '.....Your are  overweight')
                self.DietPlan.setPixmap(QPixmap('losswDietPlan.jpg'))

        else:
            self.label_3.setText('enter valid details')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

