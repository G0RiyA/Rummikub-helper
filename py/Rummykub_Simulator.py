from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QListWidget, QHBoxLayout, QListWidgetItem, QBoxLayout, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, QMimeData, QRectF, QPoint, QSize
from PyQt5.QtGui import QDrag, QIcon, QPainter, QPen, QPolygon
import sys
import card
from finder import *

class Answer(QWidget):
    def __init__(self,answer):
        super().__init__()
        self.vbox = QVBoxLayout()
        for i in answer:
            nowList = [str(card) for card in i]
            nowWidgetList = ListWidget()
            nowWidgetList.setSortingEnabled(0)
            print(nowList)
            cnt = 1
            for card in nowList:
                nowWidgetList.addItem(QListWidgetItem(QIcon("../image/" + card + ".PNG"), card))
            nowWidgetList.setViewMode(ListWidget.IconMode)
            
            #nowWidgetList.sizeH

            self.vbox.addWidget(nowWidgetList)

        # self.setGeometry(50,50,1000,600)
        self.setWindowTitle("answer")
        
        self.setLayout(self.vbox)

class ListWidget(QListWidget):
    def sizeHint(self):
        s = QSize()
        #s.setHeight(super(ListWidget,self).sizeHint().height())
        s.setWidth(300)
        return s
        

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

        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_btn_click)

        self.hbox.addWidget(self.hand_inputbox)
        self.hbox.addWidget(hand_btn)
        self.hbox.addWidget(self.table_inputbox)
        self.hbox.addWidget(table_btn)
        self.hbox.addStretch(1)
        self.hbox.addWidget(clear_btn)
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
        hands = []
        tables = []
        for i in self.hand:
            if i[-2].isalpha():
                col=i[:-1]
                num=int(i[-1])
            else:
                col=i[:-2]
                num=int(i[-2:])
            hands.append(Card(col,num))
        
        for i in self.table_card:
            if i[-2].isalpha():
                col=i[:-1]
                num=int(i[-1])
            else:
                col=i[:-2]
                num=int(i[-2:])
            tables.append(Card(col,num))
        
        answer = solver(hands,tables)

        if not answer:
            QMessageBox.about(self,"Solver","There is no answer")
        
        else:
            self.popup = Answer(answer)
            self.popup.show()




    def hand_btn_click(self):
        user_inputs = self.hand_inputbox.text()
        user_inputs = list(map(lambda x:x.strip(), user_inputs.split(',')))
        for user_input in user_inputs:
            if user_input in self.cards:
                self.card.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + user_input + ".PNG"), user_input))
                self.cards.remove(user_input)
                self.hand.append(user_input)
                self.cnt += 1
                self.hand_inputbox.setText('')

    def table_btn_click(self):
        user_inputs = self.table_inputbox.text()
        user_inputs = list(map(lambda x:x.strip(), user_inputs.split(',')))
        for user_input in user_inputs:
            if user_input in self.cards:
                self.table.insertItem(self.cnt, QListWidgetItem(QIcon("../image/" + user_input + ".PNG"), user_input))
                self.cards.remove(user_input)
                self.table_card.append(user_input)
                self.cnt += 1
                self.table_inputbox.setText('')
    
    def clear_btn_click(self):
        self.hand, self.cards = card.Cardset()
        self.table_card = []
        self.card.clear()
        self.table.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    hand, cards = card.Cardset()
    Filed = Table(hand, cards)
    Filed.show()
    app.exec_()