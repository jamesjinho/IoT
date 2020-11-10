import serial
import sys

from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *

form_class = uic.loadUiType("basic.ui")[0]
ser = serial.Serial(port='COM4', baudrate=115200)


class WindowsClass(QMainWindow, form_class):
    def __init__(self):
        super(WindowsClass, self).__init__()
        self.setupUi(self)
        exitAction = QAction(self)
        exitAction.triggered.connect(qApp.quit)

        self.ledON.clicked.connect(self.ledONFunction)
        self.ledOFF.clicked.connect(self.ledOFFFunction)

        self.printButton.clicked.connect(self.printState)

        self.quit.clicked.connect(QCoreApplication.instance().quit)

    def ledONFunction(self):
        self.stateLED.setText("Turn ON the LED")
        ser.write(b'LED ON')
        print(ser.readline())

    def ledOFFFunction(self):
        self.stateLED.setText("Turn OFF the LED")
        ser.write(b'LED OFF')
        print(ser.readline())

    def printState(self):
        print(self.stateLED.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowsClass()
    myWindow.show()
    app.exec_()
