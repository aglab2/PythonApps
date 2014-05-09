import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'utf-8')
        
        print("Got: {}".format(data))
        response = bytes(data.capitalize(), 'utf-8')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer): pass

HOST, PORT = "localhost", 0

server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
ip, port = server.server_address

print(ip, port)

server.serve_forever()