import sys
from PySide import QtGui
#виджет - некий примитив, который ожет выполнять некоторую фкнциональность (кнопки, окна, слайжеры)

app = QtGui.QApplication(sys.argv) #объект приложение
wid = QtGui.QWidget()

wid.resize(250, 150)
wid.setWindowTitle('Hello Python')
wid.show()

sys.exit(app.exec_()) #корректное завершение

#иерархическая структура