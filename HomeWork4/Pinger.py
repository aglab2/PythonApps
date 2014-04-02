from argparse import ArgumentParser
import subprocess
from threading import Thread

def pinger(server, outf, verbosity=0):
    if verbosity:
        print('Send request to server', server)
        
    response = subprocess.call(["ping", "-c", "1", server], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    
    if verbosity:
        print('Got responce', response, 'from server', server)
    if response == 0:
        outf.write(server+'\n')

parser = ArgumentParser(description='Process servers')
parser.add_argument('-v', action="store_true", help='verbose output')
parser.add_argument('servers', metavar='serv', type=str, nargs='+', help='Servers to ping')
parser.add_argument('-F', metavar='file', type=str, default='log', help = 'File to write servers')

args = parser.parse_args()
outf = open(args.F, 'w')
for server in args.servers:   
    t = Thread(target=pinger, args=(server, outf, args.v)) 
    t.start()
    t.join()
outf.close()