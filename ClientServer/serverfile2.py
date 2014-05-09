import tempfile
import socketserver

HOST, PORT = "localhost", 9999
BUFSIZE = 128

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler): 
    def handle(self):
        #f = open('tmp_{}'.format(threading.current_thread().ident), 'wb')
        with tempfile.TemporaryFile() as f:
            print('START WRITE')
            buf = self.request.recv(BUFSIZE)
            while buf:
                try:
                    f.write(buf)
                except Exception as e: print('ERROR: {}'.format(e))  
                buf = self.request.recv(BUFSIZE)
            f.seek(0)
            print('END WRITE')

            print('START SEND')
            buf = f.read(BUFSIZE)
            while buf:
                self.request.send(buf) 
                buf = f.read(BUFSIZE)
            print('END SEND')
            print()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer): pass

server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
server.serve_forever()