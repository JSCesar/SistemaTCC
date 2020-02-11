from gui.JanelaPrincipal import Ui_MainWindow
import cv2
from PyQt5 import QtWidgets

from PyQt5.QtCore import pyqtSlot
from gui.MainWidget import MainWidget


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = MainWidget()
        self.setCentralWidget(self.widget)
        self.show()



