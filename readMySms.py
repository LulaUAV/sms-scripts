import serial
import time
class TextMessage:
    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyACM0', 460800, timeout=5) #for mine this was ttyUSB0 but could be ttyUSB1 etc. good idea to runs ls usb and find out that way
        time.sleep(1)

    def read(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')# put in textmode
        time.sleep(1)
        self.ser.write('''AT+CMGL="ALL"''' + '''\r''') #fetch all sms's
        #self.ser.write('''AT+CMGR="3"''' + '''\r''')
        read = self.ser.readlines()
        for msg in read:
          #if "+CMGL" in msg: #+CMGL looks for all SMS messages
          print msg

    def disconnectPhone(self):
        self.ser.close()

sms = TextMessage()
sms.connectPhone()
sms.read()
sms.disconnectPhone()
raw_input("Press anykey to exit")
