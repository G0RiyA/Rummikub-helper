from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QListWidget, QHBoxLayout, QListWidgetItem, QBoxLayout
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QIcon
import sys
import card

class FiledView(QWidget):
    def __init__(self, p, a):
        super().__init__()
        self.p = p
        self.a = a
        self.initUI()
    
    def initUI(self):
        self.setAcceptDrops(True)

        self.player = QListWidget()
        self.ai = QListWidget()
        self.filed = QListWidget()


        self.player.setViewMode(QListWidget.IconMode)
        self.player.setAcceptDrops(True)
        self.player.setDragEnabled(True)

        self.ai.setViewMode(QListWidget.IconMode)
        self.ai.setAcceptDrops(True)
        self.ai.setDragEnabled(True)

        self.filed.setViewMode(QListWidget.IconMode)
        self.filed.setAcceptDrops(True)
        self.filed.setDragEnabled(True)

        self.setGeometry(300,350,1000,600)
        
        self.big = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.small = QBoxLayout(QBoxLayout.TopToBottom)
        self.small.addWidget(self.player)
        self.small.addWidget(self.ai)

        self.big.addWidget(self.filed)
        self.big.addLayout(self.small)
        

        cnt = 1
        for i in self.p:
            self.player.insertItem(cnt, QListWidgetItem(QIcon("../image/" + i + ".PNG"), i))
            cnt += 1
        cnt = 1
        for i in self.a:
            self.ai.insertItem(cnt, QListWidgetItem(QIcon("../image/" + i + ".PNG"), i))
            cnt += 1
        

        self.setWindowTitle("hi")
        
        self.setLayout(self.big)

    def dragEnterEvent(self, e):
        e.accept()
    
    def dropEvent(self, e):
        e.accept()
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    player, ai = card.cardret()
    Filed = FiledView(player,ai)
    Filed.show()
    app.exec_()