import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QHBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
import subprocess


class Windows(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Кнопка', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(200, 50)
        btn.clicked.connect(Windows.notif)
        
        exit = QPushButton('Выход', self)
        exit.resize(btn.sizeHint())
        exit.move(50, 50)
        exit.clicked.connect(QCoreApplication.instance().quit)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(exit)

        

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    def notif(self):
        subprocess.Popen(['notify-send', 'Hello World '])
