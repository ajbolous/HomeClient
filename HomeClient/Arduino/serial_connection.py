import serial

class SerialConnection(object):
    def __init__(self):
        self._serial=None

    def connect(self, port, baud):
        self._serial=serial.Serial(port,baud)
        return self._serial.isOpen()

    def disconnect(self):
        self._serial.close()

    def _read(self):
        while(True):
            data = self._serial.readline()
            print(data)

    def write_packet(self, data):
        self._serial.write(chr(200))
        for d in data:
            self._serial.write(chr(d))
        self._serial.write(chr(200))