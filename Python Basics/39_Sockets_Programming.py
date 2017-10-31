''' 
AF_INET is Address family = IPv4
TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM.
TCP/SOCK_STREAM is a connection-based protocol. The connection is established and the two parties have a conversation until the connection is terminated by one of the parties or by a network error.
UDP/SOCK_DGRAM is a datagram-based protocol. You send one datagram and get one reply and then the connection terminates.
'''

import socket

# defining the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# target host
server = 'yahoo.in'


def scanport(port):
    try:
        s.connect((server,port)) # establish connection to the port
        return True
    except:
        return False

for p in range(1,50):
    print('testing port:',p)
    if scanport(p):
        print('Port',p,'is OPEN')
    else:
        print('Port',p,'is CLOSED')
