import socket
#import sys

host = ''
port = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5) # number of connections to accept, after which incoming requests are dropped and no new connections are made

def threadedclient():
    co

#print(s.accept())
#conn, addr = s.accept()
#print('connected to: '+addr[0]+':'+str(addr[1]))   
