
from PyQt5 import QtCore, QtGui, QtWidgets
global label_2
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(877, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = QtWidgets.QWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(30, 30, 831, 451))
        self.graph.setObjectName("graph")

        self.label_2 = QtWidgets.QLabel(self.graph)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 41))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: lightgreen")
       # self.pushButton = QtWidgets.QPushButton(self.graph, clicked=lambda: self.onclick())




        self.pushButton = QtWidgets.QPushButton(self.graph)
        #self.label_2.setText('hi')

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
        self.label_2.setText(_translate("MainWindow", "Your mood status"))
        self.pushButton.setText(_translate("MainWindow","CLICK HERE"))
        self.pushButton.clicked.connect(self.onclick(self.label_2))


    def onclick(self,label4):
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

        print("The detected emotion is:", emotion_label)
        label4.setText(emotion_label)

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())