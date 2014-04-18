import sys
from PySide import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        names = ['1', '2', '3']
        grid = QtGui.QGridLayout()
        j = 0
        
        for i in names:
            button = QtGui.QPushButton(i)
            #grid.addWidget((0,0), button, (0,0))
        
        self.setLayout(grid)    
        self.setGeometry(300, 300, 250, 250) #позиционирование относительно экрана(родителя)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
    
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())