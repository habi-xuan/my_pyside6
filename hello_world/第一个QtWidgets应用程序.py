import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
# QtWidgets
# app = QApplication([])
label = QLabel("<font color=red size=40>Hello World!</font>")
# label.show()
app.exec()      # 使窗口保持显示状态
