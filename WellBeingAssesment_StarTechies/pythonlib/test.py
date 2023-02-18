import webbrowser
from threading import Event
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from plyer import notification
from win10toast import ToastNotifier

from mentalana import Ui_ThirdWindow
from physic import Ui_SecondWindow


class Ui_MainWindow(object):
    def open_physicanalysis(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_mentalanalysis(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_ThirdWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("Background-image:url(back.jpeg);")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 290, 161, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda : self.open_mentalanalysis())
        self.pushButton_2.setGeometry(QtCore.QRect(320, 290, 171, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda : self.open_physicanalysis())
        self.pushButton_3.setGeometry(QtCore.QRect(560, 290, 181, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda : self.chatgpt())

        self.pushButton4.setGeometry(QtCore.QRect(320, 450, 181, 101))
        self.pushButton4.setObjectName("pushButton4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 40))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 91, 40))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 91, 50))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def chatgpt(self):
        import openai
        from openai import Completion
        import tkinter as tk

        # Set up the OpenAI API client
        openai.api_key = "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"

        # Create the main window
        root = tk.Tk()
        root.title("ChatGPT App")
        root.configure(bg='light blue')

        # Create a text entry field and a send button
        entry = tk.Entry(root, font=('Arial', 14), bg='white', fg='black')

        # Create a text widget to display the conversation
        conversation = tk.Text(root, font=('Arial', 14), bg='white', fg='black')

        # Create a scrollbar for the conversation widget
        scrollbar = tk.Scrollbar(root, orient='vertical', command=conversation.yview)
        conversation['yscrollcommand'] = scrollbar.set

        # Create a function to clear the conversation widget
        def clear_conversation():
            conversation.delete('1.0', 'end')

        # Create a function to send a message to ChatGPT and display the response
        def send_message():
            # Get the message from the entry field
            message = entry.get()

            # Clear the entry field
            entry.delete(0, "end")

            # Use the OpenAI API to get a response from ChatGPT
            response = Completion.create(
                engine="text-davinci-002",
                prompt=message,
                max_tokens=1024,
                temperature=0.5,
            )

            # Display the message and the response in the conversation widget
            conversation.insert("end", f"You: {message}\n")
            conversation.insert("end", f"Bot: {response.get('choices')[0].get('text')}\n")

        # Create the send button
        send_button = tk.Button(root, text="Send", font=('Arial', 14), command=send_message, bg='white', fg='black')

        # Create the clear button
        clear_button = tk.Button(root, text='Clear', command=clear_conversation, bg='white', fg='black')

        # Pack the widgets into the window
        entry.pack()
        send_button.pack()
        clear_button.pack()
        conversation.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Run the Tkinter event loop
        root.mainloop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Notifications"))
        self.pushButton.clicked.connect(self.notify)
        self.pushButton_2.setText(_translate("MainWindow", "Mental Health"))
        self.pushButton_3.setText(_translate("MainWindow", "Physical Health"))
        self.pushButton4.setText(_translate("MainWindow", "CHAT BOT"))
        self.label.setText(_translate("MainWindow", "Name :Shrutika"))
        self.label_2.setText(_translate("MainWindow", "Age :25 "))
        self.label_3.setText(_translate("MainWindow", "Gender : F"))

    def notify(self):
        c = 0;
        toaster = ToastNotifier()
        while c<4:
            # time.sleep(10)
            #Event().wait(5)
            notification.notify(
                title="Water Break",
                message="PLEASE TAKE WATER",

                # displaying time
                timeout=2
            )
            # waiting time
            c=c+1;
            # time.sleep(10)
            #Event().wait(5)

            # time.sleep(10)
            #Event().wait(5)
            notification.notify(
                title="SCREENTIME EXCEEDED",
                message="Please close your eyes for sometime you have exceeded the screen time limit.",

                # displaying time
                timeout=2
            )
            # waiting time
            # time.sleep(10)
            #Event().wait(5)





import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())