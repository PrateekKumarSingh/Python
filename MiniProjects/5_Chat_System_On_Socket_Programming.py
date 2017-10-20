import socket
import sys
from _thread import *
import time

# function to broadcast messages to telnet client
def broadcast_message(message, conn):
    for c, n in client.items():
        # condition to avoid broadcasting messages
        # to the client sending the message
        print(message)
        if c!=conn and n[0]:
            c.sendall(str.encode(message))

# generate timestamp
def get_timestamp():
    return time.strftime("%H:%M")

# remove a user from chat room
def kick_user():
    return ''

# make first user admin
def make_admin():
    return ''

# close user connection
def close_connection():
    return ''

def get_online_users():
    response = '\r\n Following users are online, Total:{0}\r\n'.format(len(client))
    table = ''
    table += '\r{0}{1}\r\n'.format('IPADDRESS:PORT'.center(20), 'NAME'.center(20))

    for c, n in client.items():
        table += '\r{1}{0}\r\n'.format(str(n[0]).center(20), str(n[1]+":"+n[2]).center(20))

    response += table + '\r\n'
    return response

# client function
def threaded_client(conn, ipaddress, port):
    name = ""
    conn.sendall(str.encode('Enter your name: '))

    while True:
        nameData = conn.recv(4048)
        if '\r\n' in nameData.decode('utf-8'):
            client[conn][0]=name
            break
        elif not nameData:
            break
        else:
            name += nameData.decode('utf-8')

    conn.sendall(str.encode('{1} [Server] Hi \'{0}\', Welcome to the chat room!\r\n{1} [Server] Type **help to get HELP information\r\n'.format(name,get_timestamp())))

    broadcast_message('\r{1} [Server] \'{0}\' joined the chat.\r\n'.format(name,get_timestamp()), conn)

    reply = ""
    while True:
        data = conn.recv(4048)
        reply += data.decode('utf-8')
        if '\n' in data.decode('utf-8'): # to listen carriage return
            reply = "{2} [{0}] {1}".format(name,reply,get_timestamp())
            broadcast_message(reply, conn)
            reply = ""
        elif '\b' in data.decode('utf-8'): # for backspace deletion
            reply = reply[0:len(reply) - 2]

        print(reply)
        # Liteners for commands typed in telnet client
        if reply=='**help':
            conn.sendall(str.encode(helpmessage))
            reply = ""
        elif reply=='**users':
            conn.sendall(str.encode(get_online_users()))
            reply = ""

        if not data:
            break
    conn.close()

# main
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
helpmessage = '''\r\n ----------------------------------------------------------\r
  HELP - Type below command(s) to get response from server\r
 ----------------------------------------------------------\r
  **help  - Get Help information\r
  **users - Get number of people online\r
 ----------------------------------------------------------\r
'''

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')
client = {}
while True:
    conn, addr = s.accept()
    ipaddress = addr[0]
    port = str(addr[1])
    client[conn]=['',ipaddress,port]
    print('connected to: '+addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,ipaddress,port)) # start_new_thread (function, args[, kwargs])
