from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QListWidget, QHBoxLayout, QListWidgetItem, QBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QMimeData, QRectF, QPoint
from PyQt5.QtGui import QDrag, QIcon, QPainter, QPen, QPolygon
import sys
import card

class Table(QWidget):
    def __init__(self, hand, cards):
        super().__init__()
        self.hand = hand
        self.cards = cards
        self.initUI()
    
    def initUI(self):
        self.card = QListWidget()
        self.card.setViewMode(QListWidget.IconMode)
        self.card.setAcceptDrops(True)
        self.card.setDragEnabled(True)
        self.card.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
       
        self.vbox = QVBoxLayout() # main layout
        self.hbox = QHBoxLayout() # sub layout

        btn = QPushButton("Drow")
        btn.clicked.connect(self.btn_click)
        self.hbox.addStretch(1)
        self.hbox.addWidget(btn)

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.card)
        self.cnt = 1
        for i in self.hand:
            self.card.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + i + ".PNG"), i))
            self.cnt += 1
        
        self.setGeometry(50,50,1000,600)
        self.setWindowTitle("rummykub")
        
        self.setLayout(self.vbox)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.red)
        painter.drawLine(11,200,989,200)

    def btn_click(self):
        ret1, ret2 = card.Drow(self.cards)        
        self.hand.append(ret1)
        self.card.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + ret1 + ".PNG"), ret1))
        self.cards = ret2

if __name__=='__main__':
    app = QApplication(sys.argv)
    hand, cards = card.Cardset()
    Filed = Table(hand, cards)
    Filed.show()
    app.exec_()