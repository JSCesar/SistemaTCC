

class ModelReader:
    def __init__(self,fileName):
        self.fileName = fileName
        self.file = None
    def readFile(self):
        self.fileName = '../img/'+self.fileName
        self.file = open(self.fileName)
        self.getData()

    def getData(self):
        if self.file != None:
            for line in self.file:
                print(line)

        print('fim do arquivo...')