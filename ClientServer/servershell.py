import socketserver
from subprocess import Popen, PIPE

HOST, PORT = "localhost", 9999
BUFSIZE = 1024

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler): 
    def handle(self):
        command = str(self.request.recv(BUFSIZE), 'utf-8')

        print('GET COMMAND')
        process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        print('START SEND')
        out = process.communicate()
        if out[0] != None: self.request.sendall(out[0]) 
        if out[1] != None: self.request.sendall(out[1]) 
        print('END SEND')
        print()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer): pass

server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
server.serve_forever()