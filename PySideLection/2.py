import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        label1 = QtGui.QLabel('<font size=15>PiterPy</font>')
        label1.move(15, 30)
        label2 = QtGui.QLabel('<font size=15>PiterPy</font>')
        label2.move(35, 40)
        label2 = QtGui.QLabel('<font size=15>PiterPy</font>')
        label2.move(55, 70)
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a tooltip bro!')
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is <b>button</b> tooltip bro!')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        self.setGeometry(300, 300, 250, 250) #позиционирование относительно экрана(родителя)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
    
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())