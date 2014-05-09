import socket
import sys

HOST, PORT = 'localhost', 9999
BUFSIZE = 1024

password = input()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send(bytes(password, 'utf-8'))
sock.shutdown(socket.SHUT_WR)

out = sock.recv(BUFSIZE)
sock.close()
if out == b'OK':
    print('Access granted')
if out == b'NO':
    print('Access denied')
    sys.exit()
if out == b'NEW':
    print('New password created')

while True:
    command = input()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.sendall(bytes(password, 'utf-8'))
        out = sock.recv(BUFSIZE)

        if out == b'NO':
            print('Access denied')
            sys.exit()    
        if out == b'OK':
            sock.sendall(bytes(command, 'utf-8'))
            buf = sock.recv(BUFSIZE)
            while buf:
                print(str(buf, 'utf-8'), end='')
                buf = sock.recv(BUFSIZE)
    except Exception as e: 
        print('File send error: {}'.format(e))
    finally:
        sock.close()
