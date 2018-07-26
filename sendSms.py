import serial
import time

class TextMessage:
    def __init__(self, recipient="8442462790", message="TextMessage.content not set."):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyACM0', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
        time.sleep(1)

    def sendMessage(self):
        print 'Sending message...'
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def disconnectPhone(self):
        print 'Disconneting phone...'
        self.ser.close()

sms = TextMessage("8442462790","SMS Message enviado desde Linux Mint")
sms.connectPhone()
for x in range(0,3):
    sms.sendMessage()
sms.disconnectPhone()
print "message sent successfully"