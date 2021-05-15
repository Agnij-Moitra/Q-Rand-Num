import sys
import os
import importlib.util
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):

    def __init__(self):
        self.num = 0

    def load_module(self, file_name, module_name):
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

    def show_popup(self, title, content, type):
        msg = QMessageBox()
        msg.setWindowTitle(str(title))
        msg.setText(str(content))

        if type == "info":
            msg.setIcon(QMessageBox.Information)

        if type == "warning":
            msg.setIcon(QMessageBox.Warning)

        exit_show_popup = msg.exec_()

    def main(self):
        if self.num == 0:
            self.show_popup(
                "Error", f"Please Enter An Integer First", "warning")
            return

        QRand = self.load_module("QRandNumGen.py", "main")
        generated = QRand.main(self.num)

        self.show_popup("Quantum Random Bit String Generator",
                        f"Your Random Bit String is {generated}", "info")

    def pushButton_handler(self):
        self.main()

    def get_text(self):
        try:
            buffer = int(self.lineEdit.text())
        except ValueError:
            self.show_popup("Error", "Please Enter An Integer", "warning")
            return

        if buffer < 33 and buffer > 1:
            buffer -= 1
            self.num = buffer
            return

        else:
            self.show_popup(
                "Error", "Please Enter A Number Between 1 and 32 (Upper And Lower Limits Are Included)", "warning")
            return

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "fractal-hassan-XoNj0ulsn1Y-unsplash.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 771, 71))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: bold 25pt \"Sans Serif\";\n"
                                   "gridline-color: rgb(85, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 60, 671, 291))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 20pt \"Sans Serif\";\n"
                                   "gridline-color: rgb(85, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 310, 501, 155))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 20pt \"Sans Serif\";\n"
                                   "gridline-color: rgb(85, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 490, 251, 61))
        self.pushButton.setStyleSheet("background-color: lightgreen;\n"
                                      "color: black;\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: black;\n"
                                      "font: bold 20px \"Newspaper\";\n"
                                      "padding: 6px;\n"
                                      "min-width: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 360, 171, 51))
        self.lineEdit.setStyleSheet("font: 16pt \"Sans Serif\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.get_text)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "Quantum Random Bit String Generator", "Quantum Random Bit String Generator"))
        self.label_2.setText(_translate(
            "MainWindow", "Quantum Random Bit String Generator"))
        self.label_3.setText(_translate("MainWindow", "This will use a Quantum Computer\n"
                                        "to generate True random bit strings.\n"
                                        "Unlike Classical Computer which generates\n"
                                        "pseudo bit string. It has a good\n"
                                        "amount applications in crytography and even\n"
                                        "Tech Giants like Samsung are using it."))
        self.label_4.setText(_translate("MainWindow", "Enter Length of digits you want:\n"
                                        "Note: Due to the current hardware\n"
                                        "limitation you can enter 32 at max.\n"
                                        "When you're done press enter and\n"
                                        "please wait for 1 - 2 min"))
        self.pushButton.setText(_translate("MainWindow", "Generate 😀!"))
        self.pushButton.clicked.connect(self.pushButton_handler)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
