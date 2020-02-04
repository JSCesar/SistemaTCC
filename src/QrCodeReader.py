from cv2 import cv2
from scipy.spatial import distance as dist

class QrCodeReader:
    def __init__(self):
        self.QrCodeDetector = cv2.QRCodeDetector()
        self.dados = None
        self.box = None
        self.rectfiedImage = None

    def read(self,imagem):
        self.dados,self.box,self.rectfiedImage = self.QrCodeDetector.detectAndDecode(imagem)
        if len(self.dados) > 0:
            return self.dados,self.box,self.rectfiedImage
        return None;

    #calcula a proporcao de altura e largura do qrcode para auxiliar no posicionamento da camera
    def getProporcao(self,box):
        p1 = dist.euclidean(tuple(box[0][0]), tuple(box[1][0]))
        p2 = dist.euclidean(tuple(box[1][0]), tuple(box[2][0]))
        proporcao = p1 / p2
        return proporcao

