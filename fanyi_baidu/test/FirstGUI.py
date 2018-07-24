# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('logout.png'), '&退出', self)
        # 设置对应快捷键
        exitAction.setShortcut('Ctrl+Q')
        # 设置状态栏提示信息
        exitAction.setStatusTip('退出应用程序')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        # 添加一个菜单，显示为文件
        fileMenu = menubar.addMenu('&文件')
        # 将自定义的抽象动作，添加至文件菜单中
        fileMenu.addAction(exitAction)
        EditeMenu = menubar.addMenu('&编辑')
        EditeMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('菜单栏')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())