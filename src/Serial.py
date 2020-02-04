import serial
from Util.States import States

class ControleSerial:
    def __init__(self):
        self.cs = serial.Serial('COM3', 9600,timeout=.01)
        self.state = States.AGUARDANDO

    def verficaConexao(self):
        if self.cs.is_open:
            return True
            #teste = self.cs.write("teste\n".encode())
            #result = self.cs.readline(255)
        else:
            print('Serial não conectada')
            return False

    def aumentaAngulo(self):
        self.cs.write("acima\n".encode())
        self.setState(States.ENVIADO)
        return True

    def diminuiAngulo(self):
        self.cs.write("abaixo\n".encode())
        self.setState(States.ENVIADO)
        return True

    def getStateSerial(self):
        result = self.cs.readline(255)
        print(result)
        return self.state

    def setState(self, state):
        if state == 'aguardando\n':
            self.state = States.AGUARDANDO
        elif state == 'executado\n':
            self.state = States.LIVRE