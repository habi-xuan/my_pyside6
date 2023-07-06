import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.my_name = ['xuan', 'xing_yuan', '汪星人', '兴源']

        # 添加点击按钮
        self.button = QtWidgets.QPushButton('点击这里')
        # 添加文本 并对齐
        self.text = QtWidgets.QLabel('猜猜我是谁', alignment=QtCore.Qt.AlignCenter)

        # 垂直布局
        self.layout = QtWidgets.QVBoxLayout(self)
        # 将标签添加到布局里
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        # 在窗口上加一个按钮，并绑定信号槽
        self.button.clicked.connect(self.magic)

    # 槽函数 点击按钮需要实现的功能
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.my_name))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
