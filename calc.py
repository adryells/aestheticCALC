import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
class Calc(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Aesthetic Calc')
        self.setFixedSize(400,400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw) 
        self.display = QLineEdit()
        self.grid.addWidget(self.display,0,0,1,5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
                '* {background: black; color: red; font-size: 30px;}'
    )
        self.setStyleSheet(
                '* {background-image: url("botart.png"); color: black; font-size: 30px;}'
    )
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.add_btn(QPushButton('1'), 1,0,1,1,None,'background: green;')
        self.add_btn(QPushButton('2'), 2,0,1,1,None,'background: green;')
        self.add_btn(QPushButton('3'), 3,0,1,1,None,'background: green;')
        self.add_btn(QPushButton('4'), 1,1,1,1,None,'background: green;')
        self.add_btn(QPushButton('5'), 2,1,1,1,None,'background: green;')
        self.add_btn(QPushButton('6'), 3,1,1,1,None,'background: green;')
        self.add_btn(QPushButton('7'), 1,2,1,1,None,'background: green;')
        self.add_btn(QPushButton('8'), 2,2,1,1,None,'background: green;')
        self.add_btn(QPushButton('9'), 3,2,1,1,None,'background: green;')
        self.add_btn(QPushButton('0'), 3,3,1,1,None,'background: green;')
        self.add_btn(QPushButton('+'), 1,3,1,1,None,'background: brown;')
        self.add_btn(QPushButton('-'), 2,3,1,1,None,'background: brown;')
        self.add_btn(QPushButton('/'), 3,3,1,1,None,'background: brown;')
        self.add_btn(QPushButton('*'), 1,4,1,1,None,'background: brown;')
        self.add_btn(QPushButton('**'), 3,5,1,1,None,'background: brown;')
        self.add_btn(QPushButton('='), 2,4,1,1,self.igual)
        self.add_btn(QPushButton('<='), 1,5,1,1, lambda: self.display.setText(self.display.text()[:-1]),'background: red;')
        self.add_btn(QPushButton('.'), 2,5,1,1,None,'background: brown;')
        self.add_btn(QPushButton('c'), 3,4,1,1, lambda: self.display.setText(''),'background: red;')
        self.setCentralWidget(self.cw)
    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None,cor = None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
        else:
            btn.clicked.connect(funcao)
        if cor:
            btn.setStyleSheet(cor)
    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText("conta invalida.")
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    qt.exec_()