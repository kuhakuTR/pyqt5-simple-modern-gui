from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import stylesheets
import sys

def main():
    class GUI(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.centerPos = QtWidgets.QDesktopWidget().availableGeometry().center()
            self.resize(1200,800)
            self.oldPos = QPoint(self.centerPos)
            qr = self.frameGeometry()
            qr.moveCenter(self.centerPos)
            self.move(qr.topLeft())
            self.setWindowTitle("Modern gui by KuhakuTR")
            self.frame = QtWidgets.QFrame(self)
            self.frame.setStyleSheet("border-radius:40px;\
                                      background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 220), stop:1 rgba(36, 36, 36, 230));")
            self.frame.setGeometry(0,0,1200,800)
            self.initUI()
        def initUI(self):
            self.exitButton = QtWidgets.QPushButton(self)
            self.exitButton.move(1150,0)
            self.exitButton.resize(50,50)
            self.exitButton.setStyleSheet(stylesheets.exitButtonStyle)
            self.exitButton.clicked.connect(self.close)
            self.exitButton.setText("✕ ")
            self.exitButton.setFont(QFont("Arial",20))
            
            self.hideButton = QtWidgets.QPushButton(self)
            self.hideButton.move(1100,0)
            self.hideButton.resize(50,50)
            self.hideButton.setStyleSheet(stylesheets.hideButtonStyle)
            self.hideButton.clicked.connect(self.showMinimized)
            self.hideButton.setText(" -")
            self.hideButton.setFont(QFont("Arial",25))
            

        def mousePressEvent(self, event):
            self.oldPos = event.globalPos()

        def mouseMoveEvent(self, event):
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def startApp():
        app = QApplication(sys.argv)
        gui = GUI()
        gui.show()
        sys.exit(app.exec_())

    startApp()


if __name__ == "__main__":
    main()