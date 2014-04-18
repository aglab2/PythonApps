import sys
from PySide import QtGui
from PySide import QtCore

class Communicate(QtCore.QObject):
    closeApp = QtCore.Signal()

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 250, 250) #позиционирование относительно экрана(родителя)
        self.setWindowTitle('Tooltips')
        self.show()

    def mousePressEvent(self, event):
        print(event)
        self.c.closeApp.emit()
    
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())