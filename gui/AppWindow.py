from gui.JanelaPrincipal import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import cv2
import numpy
from PyQt5 import QtWidgets,QtCore,QtGui
from src.QrCodeReader import QrCodeReader
from src.ModelReader import ModelReader

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from gui.MainWidget import MainWidget


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = MainWidget()
        self.setCentralWidget(self.widget)
        self.show()



