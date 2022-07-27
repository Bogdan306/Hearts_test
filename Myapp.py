from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from istr import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.text1 = QLabel(txt_hello)
        self.text2 = Qlabel(txt_instruction)
        self.btn = QPushButton(txt_next)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(text1)
        self.v_line.addWidget(text2)
        self.v_line.addWidget(btn)
        self.setLayout(self.v_line)
    def connects(self):
        pass
    def set_appear(self):
        self.setWindowTitle('Hearts Test')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
app = QApplication
main = MainWin
app.exec_()