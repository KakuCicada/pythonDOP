#-*- conding:utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 设置提示框的字体和大小
        QToolTip.setFont(QFont('Monaco',10))

        # 设置整个提示框内的内容
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 定义一个按钮的类，以及按钮的显示内容
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 设置按钮所在的位置，sizeHint自动给出一个推荐大小
        btn.resize(btn.sizeHint())
        # 按钮所在整个窗口的位置
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())