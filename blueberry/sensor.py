from serial import Serial


PORT = '/dev/ttyACM0'
RATE = 9600


class Sensor:
    def __init__(self, port=PORT, rate=RATE):
        self.serial = Serial(port, rate)

    def read(self):
        return self.serial.readline().strip()
