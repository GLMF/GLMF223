import numpy
from PySide2.QtCore import *
from PySide2.QtWidgets import *


def computeMatrix(message, textArea) -> None:
    try:
        print(message.text())
        params = list(map(int, message.text().split(',')))
        A = numpy.matrix([params[0:3], params[3:6], params[6:9]])
        B = numpy.matrix([params[9:12], params[12:15], params[15:18]])
        textArea.setText('A =\n' + str(A) + '\nB =\n' + str(B) + '\nA * B =\n' + str(A * B))
    except:
        textArea.setText('Donnez les valeurs entières de deux matrices 3x3 sous la forme : a,b,..., r')
        return None
    
    message.clear()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName('Matrix multiplication')
    textArea = QTextEdit()
    textArea.setFocusPolicy(Qt.NoFocus)
    message = QLineEdit()
    layout = QVBoxLayout()
    layout.addWidget(textArea)
    layout.addWidget(message)
    window = QWidget()
    window.setLayout(layout)
    window.show()

    message.returnPressed.connect(lambda msg=message, txtArea=textArea : computeMatrix(msg, txtArea))

    app.exec_()
