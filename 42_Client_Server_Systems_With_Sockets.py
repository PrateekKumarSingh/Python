import socket
import sys
from _thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')
def threaded_client(conn):
    conn.sendall(str.encode('Enter your name > '))
    name = ""
    while True:
        nameData = conn.recv(4048)
        if '\r\n' in nameData.decode('utf-8'):
            break
        elif not nameData:
            break
        else:
            name += nameData.decode('utf-8')

    print('\n[{0}] joined the chat\n'.format(name))

    reply = ""
    conn.sendall(str.encode('[{0}]'.format(name)))
    while True:
        data = conn.recv(4048)
        reply += data.decode('utf-8')
        if '\n' in data.decode('utf-8'):
            print("[{0}] {1}".format(name, reply))
            reply = "[Server] " + reply + "\n[{0}] ".format(name)
            conn.sendall(str.encode(reply))
            reply = ""
        elif '\b' in data.decode('utf-8'): # for backspace deletion
            reply = reply[0:len(reply) - 2]

        if not data:
            break
    conn.close()

while True:
    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,))
