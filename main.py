import sys
from pathlib import Path

from PySide6.QtCore import QObject, Slot, Signal , Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine




class Bridge(QObject):

    textChanged = Signal()

    def __init__(self):
        super().__init__()
        self._a = [1, 2, 3, 4, 5]

    @Property(list, notify=textChanged)
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a=value
        self.textChanged.emit()

    @Slot(str)
    def appendValue(self, value):
        self._a.append(value)
        self.textChanged.emit()

    @Slot(result=list)
    def getText(self):
        return self._a

    @Slot(str)
    def displayText(self):
        print("from python1:",self._a)


    @Slot(str, result=str)
    def getColor(self, s):
        if s.lower() == "red":
            return "#ef9a9a"
        elif s.lower() == "green":
            return "#a5d6a7"
        elif s.lower() == "blue":
            return "#90caf9"
        else:
            return "white"

    @Slot(float, result=int)
    def getSize(self, s):
        size = int(s * 34)
        if size <= 0:
            return 1
        else:
            return size

    @Slot(str, result=bool)
    def getItalic(self, s):
        if s.lower() == "italic":
            return True
        else:
            return False

    @Slot(str, result=bool)
    def getBold(self, s):
        if s.lower() == "bold":
            return True
        else:
            return False

    @Slot(str, result=bool)
    def getUnderline(self, s):
        if s.lower() == "underline":
            return True
        else:
            return False


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()



    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qml_file = Path(__file__).parent / 'RootWindow.qml'

    bridge=Bridge()

    bridge.textChanged.connect(bridge.displayText)

    engine.rootContext().setContextProperty("bridge", bridge)


    # #show the qml file

    engine.load(qml_file)

    sys.exit(app.exec())
