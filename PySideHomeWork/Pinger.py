#from argparse import ArgumentParser
import subprocess
import logging
from threading import Thread
from PySide import QtGui, QtCore
import sys
import queue

class pinger(QtCore.QThread):
    #updateProgress = QtCore.Signal(int)
    
    def __init__(self, in_queue, out_list, msgBox):
        self.in_queue = in_queue
        self.out_list = out_list
        self.msgBox = msgBox
        QtCore.QThread.__init__(self)

    def run(self):
        server = self.in_queue.get()
        logging.debug('Send request to server', server)
        response = subprocess.call(["ping", "-c", "1", server], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        logging.debug('Got responce', response, 'from server', server)
        if response == 0: self.out_list.append(server)
        self.in_queue.task_done()
        #self.msgBox.setValue(self.msgBox.value() + 1)

def outer(in_queue, out_list, console, button):
    in_queue.join()
    for server in out_list:
        console.append(server)

    button.clicked.emit()
    
class Example(QtGui.QWidget):
    __console_in__ = None
    __console_out__ = None
    
    def __init__(self):
        super(Example, self).__init__()
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
        
        in_queue = queue.Queue()
        out_list = list()
        
        for i in range(block_num):
            in_queue.put(doc.findBlockByLineNumber(i).text())
        
        cButton = QtGui.QPushButton()
        msgBox = QtGui.QProgressDialog()
        msgBox.setLabel(QtGui.QLabel('Working...'))
        msgBox.setCancelButton(cButton)
        msgBox.setRange(0, block_num)
        
        for i in range(block_num): pinger(in_queue, out_list, msgBox).start()#Thread(target=pinger, args=(in_queue, out_list, msgBox)).start()
        Thread(target=outer, args=(in_queue, out_list, self.__console_out__, cButton)).start()
        msgBox.exec_()
        
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
