import socket

BUFSIZE = 128
HOST, PORT = 'localhost', 9999

_write = False
_file = None

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(1)
        conn, addr = sock.accept()

        f = open('tmp', 'wb')
        print('START WRITE')
        buf = conn.recv(BUFSIZE)
        while buf:
            try:
                f.write(buf)
            except Exception as e: print('ERROR: {}'.format(e))  
            buf = conn.recv(BUFSIZE)
        print('END WRITE')
        f.close()

        print('START SEND')
        f = open('tmp', 'rb')
        buf = f.read(BUFSIZE)
        while buf:
            conn.send(buf) 
            buf = f.read(BUFSIZE)
        print('END SEND')
        f.close()
    finally:
        conn.close()
        sock.close()