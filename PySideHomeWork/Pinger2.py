from PySide import QtCore, QtGui
#import queue
import sys
#from threading import Thread
import subprocess
import logging

class PingerThread(QtCore.QThread):
    def __init__(self, server, out_list, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.server = server
        self.out_list = out_list
    
    def run(self):
        logging.debug('Send request to server', self.server)
        response = subprocess.call(["ping", "-c", "1", self.server], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        logging.debug('Got responce', response, 'from server', self.server)
        if response == 0: self.out_list.append(self.server)
        self.emit(QtCore.SIGNAL("progress()"))

class PBar(QtGui.QDialog):
    def __init__(self, maxim, parent=None):
        super(PBar, self).__init__(parent)
        self.setWindowTitle("Ping in process...")
        l = QtGui.QVBoxLayout()
        self.progressBar = QtGui.QProgressBar()
        l.addWidget(self.progressBar)
        self.setLayout(l)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(maxim)
        self.progressBar.setValue(0)

    def addValue(self):
        self.progressBar.setValue(self.progressBar.value() + 1)
        if self.progressBar.maximum() == self.progressBar.value():
            self.close()

class PingerWindow(QtGui.QWidget):
    __console_in__ = None
    __console_out__ = None
    
    def __init__(self):
        super(PingerWindow, self).__init__()
        self.initUI()
        
    def initUI(self):     
        self.__console_in__ = QtGui.QTextEdit()
        self.__console_out__ = QtGui.QTextEdit()
        self.__console_out__.setTextInteractionFlags(0) #not editable
        
        pingButton = QtGui.QPushButton("Ping")
        pingButton.clicked.connect(self.__ping_button__)
        
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Input addresses'), 0, 0)
        grid.addWidget(QtGui.QLabel('Pinged addresses'), 0, 1)
        grid.addWidget(self.__console_in__, 1, 0)
        grid.addWidget(self.__console_out__, 1, 1)
        grid.addWidget(pingButton, 2, 1)

        pingButton.resize(pingButton.sizeHint())

        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Pinger v0.1')
        self.show()
    
    def __ping_button__(self):
        doc = self.__console_in__.document()
        block_num = doc.blockCount()
        
        self.__console_out__.clear()
        
        out_list = list()        
        pBar = PBar(block_num)
        #pBar.show()
        for i in range(block_num): 
            t = PingerThread(doc.findBlockByLineNumber(i).text(), out_list, self)#Thread(target=pinger, args=(in_queue, out_list, msgBox)).start()
            QtCore.QObject.connect(t, QtCore.SIGNAL("progress()"),pBar, QtCore.SLOT("addValue()"), QtCore.Qt.QueuedConnection)
            t.start()
        pBar.exec_()

        for server in out_list:
            self.__console_out__.append(server)

app = QtGui.QApplication(sys.argv)
ex = PingerWindow()
sys.exit(app.exec_())
