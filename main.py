import sys
import random
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.drawCircle)
        self.r = None

    def drawCircle(self):
        self.r = random.randint(10, 200)
        self.color = QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.repaint()

    def paintEvent(self, qp):
        if self.r:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(self.color)
            qp.drawEllipse(int(self.width() / 2 - self.r), int(self.height() / 2 - self.r / 2), self.r * 2, self.r * 2)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
