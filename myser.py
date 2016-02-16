import serial
import thread

def recieve(ser,par):
    while True:
        if(ser.inWaiting()>0):
            str = ser.read(10)
            print(str),
        
ser = serial.Serial(port='/dev/ttyUSB0',baudrate= 19200,timeout=10)
thread.start_new_thread(recieve,(ser,0))

while True:
    data = raw_input(">")
    ser.write(b'{}\r\n'.format(data))
