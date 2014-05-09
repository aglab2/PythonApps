import socket
import sys

BUFSIZE = 128
HOST, PORT = 'localhost', 9999

try:
    file = sys.argv[1]
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        
        with open(file, 'rb') as f:
            buf = f.read(BUFSIZE)
            while buf:
                sock.send(buf)
                buf = f.read(BUFSIZE)
            print('OK SEND')
            sock.shutdown(socket.SHUT_WR)

        with open('out', 'wb') as f:
            buf = sock.recv(BUFSIZE)
            while buf:
                f.write(buf)
                buf = sock.recv(BUFSIZE)
            print('OK WRITE')
            sock.close()
    except Exception as e: 
        print('File send error: {}'.format(e))
        raise e
    finally:
        sock.close()
except Exception: print('Failed: sys.argv error')