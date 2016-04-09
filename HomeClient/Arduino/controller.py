from Arduino.serial_connection import SerialConnection

class Pin(object):
    def __init__(self, pin, type):
        self._pin = pin
        self._type = type
        self._value = 0

    def toPacket(self):
        return [self._type,self._pin,self._value]



class Controller(object):
    def __init__(self, port, baud):
        self._serial = SerialConnection()
        self._serial.connect(port,baud)
        self._pins = {}

    def changePin(self,pin, value):
        if pin in self._pins:
            p = self._pins[pin]
            p._value = value
            self._serial.write_packet(p.toPacket())

    def addPins(self,pins):
        for pin in pins:
            self._pins[pin._pin] = pin

    def addPin(self,pin):
        self._pins[pin._pin] = pin


c = Controller('/dev/ttyACM0',9600)
for i in range(7,14):
    p = Pin(i,2)
    c.addPin(p)

