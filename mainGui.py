from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
import sys

def main():
    class GUI(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.centerPos = QtWidgets.QDesktopWidget().availableGeometry().center()
            self.resize(1200,800)
            qr = self.frameGeometry()
            qr.moveCenter(self.centerPos)
            self.move(qr.topLeft())
            self.setWindowTitle("Modern gui by KuhakuTR")
            self.frame = QtWidgets.QFrame(self)
            self.frame.setStyleSheet("border-radius:40px;\
                                      background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(6, 44, 48, 255), stop:1 rgba(5, 89, 91, 255))")
            self.frame.setGeometry(0,0,1200,800)
            self.initUI()
        def initUI(self):
            self.exitButton = QtWidgets.QPushButton(self)
            self.exitButton.move(1150,0)
            self.exitButton.resize(50,50)
            self.exitButton.setStyleSheet("QPushButton{background-color:#B20600;\
                                           border-top-Right-radius:40px;}\
                                           QPushButton:hover{background-color:#e60800;}\
                                           QPushButton:pressed{background-color:#cc0700;\
                                           padding: 1px -1px -1px 1px}")
            self.exitButton.clicked.connect(self.close)
            self.exitButton.setText("✕ ")
            self.exitButton.setFont(QFont("Arial",20))
            
            self.hideButton = QtWidgets.QPushButton(self)
            self.hideButton.move(1100,0)
            self.hideButton.resize(50,50)
            self.hideButton.setStyleSheet("QPushButton{background-color:#525E75;\
                                           border-bottom-Left-radius:40px;}\
                                           QPushButton:hover{background-color:#5e6d87;}\
                                           QPushButton:pressed{background-color:#546078;\
                                           padding: 1px -1px -1px 1px}")
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