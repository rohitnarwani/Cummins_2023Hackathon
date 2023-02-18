# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mentalanalysis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sklearn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
class Ui_ThirdWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.week1 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.week1w)
        self.week1.setGeometry(QtCore.QRect(20, 50, 171, 51))
        self.week1.setObjectName("week1")
        self.week3 = QtWidgets.QPushButton(self.centralwidget)
        self.week3.setGeometry(QtCore.QRect(380, 50, 171, 51))
        self.week3.setObjectName("week3")
        self.week2 = QtWidgets.QPushButton(self.centralwidget)
        self.week2.setGeometry(QtCore.QRect(200, 50, 171, 51))
        self.week2.setObjectName("week2")
        self.week4 = QtWidgets.QPushButton(self.centralwidget)
        self.week4.setGeometry(QtCore.QRect(560, 50, 171, 51))
        self.week4.setObjectName("week4")
        self.labelrecog = QtWidgets.QLabel(self.centralwidget)
        self.labelrecog.setGeometry(QtCore.QRect(200,200,171,51))
        self.recog = QtWidgets.QPushButton(self.centralwidget)
        self.recog.setGeometry(QtCore.QRect(20, 200, 171, 51))
        self.recog.setObjectName("recog")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 31))
        self.label.setObjectName("label")
        self.a = QtWidgets.QLabel(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(20, 300, 100, 51))
        self.b = QtWidgets.QLabel(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(20, 400, 100, 51))
        self.c = QtWidgets.QLabel(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(20, 500, 100, 51))
        self.d = QtWidgets.QLabel(self.centralwidget)
        self.d.setGeometry(QtCore.QRect(20, 600, 100, 51))
        self.e = QtWidgets.QLabel(self.centralwidget)
        self.e.setGeometry(QtCore.QRect(20, 700, 100, 51))
        self.f = QtWidgets.QLabel(self.centralwidget)
        self.f.setGeometry(QtCore.QRect(20, 800, 100, 51))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
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
        self.week1.setText(_translate("MainWindow", "WEEK-1"))
        self.week1.clicked.connect(self.week1w)
        self.week3.setText(_translate("MainWindow", "WEEK-3"))
        self.week3.clicked.connect(self.week3w)
        self.week2.setText(_translate("MainWindow", "WEEK-2"))
        self.week2.clicked.connect(self.week2w)
        self.week4.setText(_translate("MainWindow", "WEEK-4"))
        self.week4.clicked.connect(self.week4w)
        self.recog.setText(_translate("MainWindow", "MOOD"))
        self.recog.clicked.connect(self.moodRec)
        self.a.setText(_translate("MainWindow", "0 - Angry"))
        self.b.setText(_translate("MainWindow", "2 - Disgust"))
        self.c.setText(_translate("MainWindow", "3 - Fear"))
        self.d.setText(_translate("MainWindow", "4 - Happy"))
        self.e.setText(_translate("MainWindow", "5 - Neutral"))
        self.f.setText(_translate("MainWindow", "6 - Sad"))

        self.label.setText(_translate("MainWindow", "Weekly Mood Analysis"))

    def moodRec(self, MainWindow):
        import cv2
        import numpy as np
        import tensorflow as tf
        from tensorflow import keras

        # Open the default camera
        cap = cv2.VideoCapture(0)

        # Capture an image
        ret, frame = cap.read()

        # Release the camera
        cap.release()

        # Save the image as a file
        cv2.imwrite("image(1).jpg", frame)
        # Load the image
        img = cv2.imread("image(1).jpg", cv2.IMREAD_GRAYSCALE)

        img = cv2.resize(img, (48, 48))
        img = np.array(img).reshape(-1, 48, 48, 1).astype("float32") / 255.0

        # Load the model
        model = keras.models.load_model("model.h5")

        # Predict the emotion label
        emotion_labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

        predictions = model.predict(img)

        emotion_label = emotion_labels[np.argmax(predictions[0])]

        self.labelrecog.setText(emotion_label)

    def week1w(self):
        df = pd.read_csv('week1.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()
    def week2w(self):
        df = pd.read_csv('week2.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()
    def week3w(self):
        df = pd.read_csv('week3.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()
    def week4w(self):
        df = pd.read_csv('week4.csv')
        sns.countplot(x='emotion', data=df)
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

