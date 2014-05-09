import socketserver
from subprocess import Popen, PIPE
import hashlib

HOST, PORT = "localhost", 9999
BUFSIZE = 1024

def getDigest(password):
    return hashlib.sha256(password).hexdigest()

def isPassword(password, digest):
    return getDigest(password) == digest

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler): 
    def handle(self):
        password = self.request.recv(BUFSIZE)
        try:
            with open('password', 'r') as pass_file:
                digest = pass_file.readline()
                if not isPassword(password, digest):
                    self.request.sendall(b'NO') 
                else:
                    self.request.sendall(b'OK')
        except Exception:
            command = str(self.request.recv(BUFSIZE), 'utf-8')
            if not command:
                with open('password', 'w') as pass_file:
                    digest = getDigest(password)
                    pass_file.write(digest)
                    self.request.sendall(b'NEW')
            else:
                self.request.sendall(b'NO')
            return
        
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