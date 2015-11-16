from threading import Thread


class Receiver(Thread):
    def __init__(self, pi, client_sock, client_info):
        Thread.__init__(self)
        self.pi = pi
        self.client_sock = client_sock
        self.client_info = client_info

    def run(self):
        print('accepted connection from ', self.client_info)

        try:
            while True:
                data = self.client_sock.recv(1024)
                if len(data) == 0:
                    break
                print('received: %s' % data)
                self.pi.update_device(self.client_info[0], data)
        except IOError:
            pass

        print('transmission ended')

        self.client_sock.close()

        print('client done')
