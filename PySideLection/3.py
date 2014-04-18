import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        okButton = QtGui.QPushButton("OK")
        clButton = QtGui.QPushButton("Cancel")
        
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(clButton)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 250) #позиционирование относительно экрана(родителя)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
    
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())