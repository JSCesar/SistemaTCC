
import sys

from PyQt5 import QtWidgets

from gui.AppWindow import AppWindow

app = QtWidgets.QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

