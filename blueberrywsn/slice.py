import bluetooth as bt
from threading import Event, Thread

from constants import UUID
from sensor import Sensor


INTERVAL = 1


class Slice(Thread):
    def __init__(self, local=False, interval=INTERVAL):
        Thread.__init__(self)
        self.done = None
        self.interval = interval
        self.local = local
        self.sensor = Sensor()

    def run(self):
        self.done = Event()
        while not self.done.wait(self.interval):
            info = self.sensor.read()
            if self.local:
                print info
            else:
                self.send(info)

    def send(self, info):
        # search for the server service
        service_matches = bt.find_service(uuid=UUID)

        if not service_matches:
            print('The server could not be found')

        first_match = service_matches[0]
        port = first_match['port']
        name = first_match['name']
        host = first_match['host']

        print('Connecting to \'%s\' on %s' % (name, host))

        # Create the client socket
        sock = bt.BluetoothSocket(bt.RFCOMM)
        sock.connect((host, port))
        print('Connected')

        sock.send(str(info))
        print('Info sent')

        sock.close()
        print('Conection closed')

    def stop(self):
        self.done.set()


def main():
    s = Slice()
    s.start()
    try:
        raw_input('Press any key to stop the client')
    except KeyboardInterrupt:
        print()
    finally:
        s.stop()


if __name__ == '__main__':
    main()
