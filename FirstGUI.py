#-*- conding:utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """setGeometry()做了两件事：将窗口在屏幕上显示，并设置了它的尺寸。
        setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。
        第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。"""
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())