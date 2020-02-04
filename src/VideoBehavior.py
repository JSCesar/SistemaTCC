from PyQt5 import QtCore, QtWidgets, QtGui
import cv2
import numpy as np
from src.QrCodeReader import QrCodeReader
from src.ObjectSize import ObjectSize
from src.Serial import ControleSerial
from Util.States import States
import serial

class VideoBehavior(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)
        self.qrReader = QrCodeReader()
        self.controleSerial = ControleSerial()
        self.err = 0.01

    def image_data_slot(self, image_data):

        #print(image_data)
        image = cv2.imread(image_data, cv2.IMREAD_GRAYSCALE)
        qrcode = self.qrReader.read(image_data)
        if qrcode != None:
            #verifica posicao da camera
            if self.verificaPosicao(qrcode):
                #inicia o objeto para recuperar tamanho da imagem através da webcam
                objSize = ObjectSize(image_data,1)
                objs = objSize.getSize()
                file = '../../img/'+qrcode[0]
                modelSize = objSize.getSize(file,1)
                model = objSize.getSize(file)
        else:
            cv2.rectangle(image_data, (0, 0), (100, 100), (0, 0, 255))
        self.image = self.get_qimage(image_data)

        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())
        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage
        image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    # verifica a posicao da camera através de comunicação serial
    def verificaPosicao(self,qrcode):
        serial = self.controleSerial.verficaConexao()
        prop = self.qrReader.getProporcao(qrcode[1])
        state = self.controleSerial.getState()
        print(state)
        '''if state == States.AGUARDANDO:
            if prop > 1 + self.err:
                self.controleSerial.aumentaAngulo()
            if prop < 1 - self.err:
                self.controleSerial.aumentaDiminui()
                return True
        else:
            return False'''
