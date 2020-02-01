from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QListWidget, QHBoxLayout, QListWidgetItem
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QIcon
import sys
import card

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
    
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)

        drag.exec_(Qt.MoveAction)

class FiledView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setAcceptDrops(True)

        self.myListWidget = QListWidget()
        self.myListWidget.setViewMode(QListWidget.IconMode)
        self.myListWidget.setAcceptDrops(True)
        self.myListWidget.setDragEnabled(True)

        self.setGeometry(300,350,500,300)
        
        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.myListWidget)

        l1 = QListWidgetItem(QIcon("../image/1.PNG"), "1")
        l2 = QListWidgetItem(QIcon("../image/3.PNG"), "3")
        

        self.myListWidget.insertItem(1, l1)
        self.myListWidget.insertItem(2, l2)

        self.setWindowTitle("hi")
        self.setLayout(self.hboxlayout)

        """
        self.button = Button('Button',self)
        self.button.move(100,65)
        self.setWindowTitle('Move')
        self.setGeometry(300,300,1000,800)
        """

    def dragEnterEvent(self, e):
        e.accept()
    
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        e.accept()
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    Filed = FiledView()
    Filed.show()
    app.exec_()