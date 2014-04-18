import sys
from PySide import QtGui
from PySide import QtCore

def f(x):
    print(x)

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox) 
        sld.valueChanged.connect(lcd.display)
        sld.valueChanged.connect(f)   
        
        self.setGeometry(300, 300, 250, 250) #позиционирование относительно экрана(родителя)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
    
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())