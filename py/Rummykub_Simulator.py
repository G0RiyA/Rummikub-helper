from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QListWidget, QHBoxLayout, QListWidgetItem, QBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt, QMimeData, QRectF, QPoint
from PyQt5.QtGui import QDrag, QIcon, QPainter, QPen, QPolygon
import sys
import card

class Table(QWidget):
    def __init__(self, hand, cards):
        super().__init__()
        self.hand = hand
        self.cards = cards
        self.table_card = []
        self.initUI()
    
    def initUI(self):
        self.card = QListWidget()
        self.card.setViewMode(QListWidget.IconMode)
        self.card.setAcceptDrops(True)
        self.card.setDragEnabled(True)
        self.card.setStyleSheet("background-color: rgba(255, 255, 255, 10);")

        self.table = QListWidget()
        self.table.setViewMode(QListWidget.IconMode)
        self.table.setAcceptDrops(True)
        self.table.setDragEnabled(True)
        self.table.setStyleSheet("background-color: rgba(255, 255, 255, 10);")

        self.hand_inputbox = QLineEdit()
        self.table_inputbox = QLineEdit()

        self.vbox = QVBoxLayout() # main layout
        self.hbox = QHBoxLayout() # sub layout

        draw_btn = QPushButton("Drow")
        draw_btn.clicked.connect(self.Draw_btn_click)

        solve_btn = QPushButton("Solve")
        solve_btn.clicked.connect(self.Solve_btn_click)

        hand_btn = QPushButton("Hand Add")
        hand_btn.clicked.connect(self.hand_btn_click)

        table_btn = QPushButton("Table Add")
        table_btn.clicked.connect(self.table_btn_click)

        now_btn = QPushButton("Now Filed")
        now_btn.clicked.connect(self.Now_btn_click)

        self.hbox.addWidget(self.hand_inputbox)
        self.hbox.addWidget(hand_btn)
        self.hbox.addWidget(self.table_inputbox)
        self.hbox.addWidget(table_btn)
        self.hbox.addStretch(1)
        self.hbox.addWidget(now_btn)
        self.hbox.addWidget(solve_btn)
        self.hbox.addWidget(draw_btn)
        

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.card)
        self.vbox.addWidget(self.table)
        self.cnt = 1
        for i in self.hand:
            self.card.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + i + ".PNG"), i))
            self.cnt += 1
        
        self.setGeometry(50,50,1000,600)
        self.setWindowTitle("rummykub")
        
        self.setLayout(self.vbox)
    """
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.red)
        painter.drawLine(11,200,989,200)
    """
    def Draw_btn_click(self):
        ret1, ret2 = card.Drow(self.cards)        
        self.hand.append(ret1)
        self.card.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + ret1 + ".PNG"), ret1))
        self.cards = ret2
        self.cnt += 1

    def Solve_btn_click(self):
        pass

    def hand_btn_click(self):
        user_input = self.hand_inputbox.text()
        if user_input in self.cards:
            self.card.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + user_input + ".PNG"), user_input))
            self.cards.remove(user_input)
            self.hand.append(user_input)
            self.cnt += 1
            self.hand_inputbox.setText('')

    def table_btn_click(self):
        user_input = self.table_inputbox.text()
        if user_input in self.cards:
            self.table.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + user_input + ".PNG"), user_input))
            self.cards.remove(user_input)
            self.table_card.append(user_input)
            self.cnt += 1
            self.table_inputbox.setText('')
        

    def Now_btn_click(self):
        return self.hand, self.table_card

if __name__=='__main__':
    app = QApplication(sys.argv)
    hand, cards = card.Cardset()
    Filed = Table(hand, cards)
    Filed.show()
    app.exec_()