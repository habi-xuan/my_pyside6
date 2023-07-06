# # -*- encoding:utf8 -*-

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # 点击按钮
        self.button = QtWidgets.QPushButton("Click me!")
        # 欢迎 对齐方式
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        # 将标签添加到布局里
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # 实例化 QApplication 类创建应用程序

    widget = MyWidget()     # 实例化自定义的 MyWidget 类创建图形化用户接口，也就是窗口
    widget.resize(800, 600)
    widget.show()           # 调用窗口的 show 方法，显示窗口

    sys.exit(app.exec())    # app 的exec方法来开启事件循环

