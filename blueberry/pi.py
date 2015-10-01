# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $
from threading import Thread

from bluetooth import *


class Pi:
    def __init__(self):
        self.server_sock=BluetoothSocket( RFCOMM )
        self.server_sock.bind(("",PORT_ANY))
        self.server_sock.listen(1)
        self.accept = True
        self.cont = 0
        port = self.server_sock.getsockname()[1]

        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

        advertise_service( self.server_sock, "SampleServer",
                           service_id = uuid,
                           service_classes = [ uuid, SERIAL_PORT_CLASS ],
                           profiles = [ SERIAL_PORT_PROFILE ],
        #                   protocols = [ OBEX_UUID ]
                            )
        print("Waiting for connection on RFCOMM channel %d" % port)

    def run(self):
        while self.accept:
            print("Esperando clientes")
            client_sock, client_info = self.server_sock.accept()
            t = Thread(target=self.receive, args=(client_sock,client_info,))
            t.daemon= True
            t.start()
            self.cont+=1
            print("clientes conectados "+str(self.cont))

        server_sock.close()
        print("server done")

    def stop(self):
        self.accept = False


    def receive(self, client_sock, client_info):

        print("Accepted connection from ", client_info)

        try:
            while True:
                data = client_sock.recv(1024)
                if len(data) == 0: break
                print("received [%s]" % data)
        except IOError:
            pass

        print("disconnected")

        client_sock.close()

        print("client done")


if __name__ == '__main__':

    p = Pi()
    p.run()