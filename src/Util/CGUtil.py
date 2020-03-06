

class CGUtil:

    def __init__(self, width, height):
        self.__mundoWidth = width
        self.__mundoheigth = height

    @property
    def mundoWidth(self):
        return self.__mundoWidth

    @mundoWidth.setter
    def setMundoWidth(self, value):
        self.__mundoWidth = value

    @property
    def mundoHeigth(self):
        return self.__mundoheigth

    @mundoHeigth.setter
    def setMundoHeigth(self, value):
        self.__mundoheigth = value

    def ConvertToWorld(self, poinTupple):
        px = poinTupple[0] / self.mundoWidth
        py = poinTupple[1] / self.mundoHeigth
        #print(px, py)
        return px, py

