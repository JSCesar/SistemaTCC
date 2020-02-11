import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui

from src.ObjectSize import ObjectSize
from src.QrCodeReader import QrCodeReader
from src.Serial import ControleSerial


class VideoBehavior(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)
        self.qrReader = QrCodeReader()
        #self.controleSerial = ControleSerial()
        self.err = 0.01

    def image_data_slot(self, image_data):

        #print(image_data)
        image = cv2.imread('./../img/teste.png')
        qrcode = self.qrReader.read(image)
        if qrcode != None:
            #verifica posicao da camera
             #self.verificaPosicao(qrcode):
                #inicia o objeto para recuperar tamanho da imagem através da webcam
                objSize = ObjectSize(image, 1)
                #array de objetos encontrados na cena
                objs = objSize.getSize()
                #file = '../../img/' + qrcode[0]
                file = qrcode[0]
                modelSize = objSize.getSize(file, 1)
                model = objSize.getSize(file)
                #print('modelSize' + str(modelSize))
                #print('model' + str(model))
                '''cv2.rectangle(image,
                              (modelSize[0][1][0][0], modelSize[0][1][0][1]),
                              (modelSize[0][1][2][0], modelSize[0][1][2][1]),
                              (255, 0, 0)
                              )'''
                #modelSize são as bordas do dado
                for ob in modelSize:
                    for pt in ob:
                        if type(pt) is np.ndarray:
                            cv2.rectangle(image, (pt[0][0], pt[0][1]), (pt[2][0], pt[2][1]), (0, 255, 0))
                #model são os desenhos do dado
                for ob in model:
                    for pt in ob:
                        if type(pt) is np.ndarray:
                            cv2.rectangle(image, (pt[0][0], pt[0][1]), (pt[2][0], pt[2][1]), (0, 255, 0))
                        if type(pt) is tuple:
                            cv2.circle(image, (int(pt[0]), int(pt[1])), 5, (0, 255, 0))


                cv2.rectangle(image, (objs[-1][1][0][0], objs[-1][1][0][1]), ( objs[-1][1][2][0],objs[-1][1][2][1] ), (0, 0, 255))
                cv2.circle(image, (int(objs[-1][2][0]), int(objs[-1][2][1])) , 5, (255,0,0))

        else:
            cv2.rectangle(image_data, (0, 0), (100, 100), (0, 0, 255))
        self.image = self.get_qimage(image)

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
