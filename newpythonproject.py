#import subprocess
import sys
import Windows
from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtCore import Qt
 
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Windows.Windows()
#    w.setWindowFlags(Qt.FramelessWindowHint)
    
    sys.exit(app.exec_())
# subprocess.Popen(['notify-send', 'TEst'])