import socket

HOST, PORT = 'localhost', 9999
BUFSIZE = 1024

while True:
    command = input()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.send(bytes(command, 'utf-8'))
        
        buf = sock.recv(BUFSIZE)
        while buf:
            print(str(buf, 'utf-8'), end='')
            buf = sock.recv(BUFSIZE)

    except Exception as e: 
        print('File send error: {}'.format(e))
    finally:
        sock.close()
