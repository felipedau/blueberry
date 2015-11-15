# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
from copy import deepcopy
from threading import Lock, Thread

from bluetooth import *

from constants import UUID
from receiver import Receiver


class Pi(Thread):
    def __init__(self):
        Thread.__init__(self)

        self._devices = {}
        self._lock_devices = Lock()

        self.server_sock=BluetoothSocket( RFCOMM )
        self.server_sock.bind(("",PORT_ANY))
        self.server_sock.listen(1)
        self.accept = True
        self.cont = 0
        port = self.server_sock.getsockname()[1]

        advertise_service( self.server_sock, "SampleServer",
                           service_id = UUID,
                           service_classes = [ UUID, SERIAL_PORT_CLASS ],
                           profiles = [ SERIAL_PORT_PROFILE ],
        #                   protocols = [ OBEX_UUID ]
                            )
        print("Waiting for connection on RFCOMM channel %d" % port)

    @property
    def devices(self):
        self._lock_devices.acquire()
        devs = deepcopy(self._devices)
        self._lock_devices.release()
        return devs

    def run(self):
        while self.accept:
            print("Esperando clientes")
            client_sock, client_info = self.server_sock.accept()
            r = Receiver(self, client_sock, client_info)
            r.daemon = True
            r.start()
            self.cont+=1
            print("clientes conectados "+str(self.cont))

        server_sock.close()
        print("server done")

    def stop(self):
        self.accept = False

    def update_device(self, device, data):
        self._lock_devices.acquire()
        self._devices[device] = data
        self._lock_devices.release()


def main():
    p = Pi()
    p.start()
    try:
        raw_input('Press any key to stop the server\n')
    except KeyboardInterrupt:
        pass
    finally:
        p.stop()


if __name__ == '__main__':
    main()
