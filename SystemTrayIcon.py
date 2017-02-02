import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QSystemTrayIcon

class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        super(SystemTrayIcon, self).__init__(icon, parent)
        menu = QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(parent.close)
        self.setContextMenu(menu)
        self.activated.connect(parent.show)