from PySide import QtCore, QtGui
import sys

class PyMage(QtGui.QMainWindow):
    def __init__(self):
        super(PyMage, self).__init__()
        self.__initUI__()
        
    def __initUI__(self):
        self.printer = QtGui.QPrinter()
        self.scaleFactor = 0.0

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,
                QtGui.QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.setCentralWidget(self.scrollArea)


        self.openAct = QtGui.QAction("&Open", self, shortcut="Ctrl+O", triggered=self.open)
        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",  triggered=self.close)
        self.zoomInAct = QtGui.QAction("Zoom &In", self, shortcut="Ctrl++", triggered=self.zoomIn)
        self.zoomOutAct = QtGui.QAction("Zoom &Out", self, shortcut="Ctrl+-", triggered=self.zoomOut)
        self.normalSizeAct = QtGui.QAction("&Normal Size", self, shortcut="Ctrl+S", triggered=self.normalSize)

        self.fileMenu = QtGui.QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QtGui.QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)

        self.setWindowTitle("PyMage")
        self.resize(500, 400)

    def open(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.currentPath())[0]
        if fileName:
            image = QtGui.QImage(fileName)
            if image.isNull():
                QtGui.QMessageBox.information(self, "PySide", "Failed to open {}.".format(fileName))
                return

            self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            
            self.imageLabel.adjustSize()

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value() + ((factor - 1) * scrollBar.pageStep()/2)))

app = QtGui.QApplication(sys.argv)
pyMage = PyMage()
pyMage.show()
sys.exit(app.exec_())