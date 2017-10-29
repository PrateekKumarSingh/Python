import socket
import sys
from _thread import *
import time

# generate timestamp
def get_timestamp():
    return time.strftime("%H:%M:%S")

# get current chat room admin
def get_chat_room_admin():
    for c, n in client.items():
        if(n[3]==True):
            return n[0]

# remove a user from chat room
def poke(conn):
    username = ''
    #conn.sendall(str.encode('\r\nEnter the username to poke: '))
    while True:
        data = conn.recv(4048)
        if '\r\n' in data.decode('utf-8'):
            break
        elif not data:
            break
        else:
            username += data.decode('utf-8')

    for c, n in client.items():
        if(n[0]==username):
            log('{0} is poking {1}'.format(client[conn][0], username))
            c.sendall(str.encode('{0} [Server] \'{1}\' just poked you privately.\r\n'.format(get_timestamp(),client[conn][0])))

def check_if_username_exist(name):
    for c,n in client.items():
        if n[0]==name:
            return True

# function to broadcast messages to all telnet client except the sender
def broadcast_except_sender(message, conn):
    log(message)
    for c, n in client.items():
        # condition to avoid broadcasting messages
        # to the client sending the message
        if c!=conn and n[0]:
            c.sendall(str.encode(message))

# function to broadcast messages to all telnet client
def broadcast(message):
    log(message)
    for c, n in client.items():
        c.sendall(str.encode(message))

# send private messages to a person in chat room
def send_private_message(conn):
    username = ''
    while True:
        data = conn.recv(4048)
        if '\r' in data.decode('utf-8'):
            break
        elif not data:
            break
        else:
            username += data.decode('utf-8')

    conn.sendall(str.encode('\r\nMessage: '))
    # to capture the private message
    privatemessage = ''
    while True:
        data = conn.recv(4048)
        if '\r\n' in data.decode('utf-8'):
            break
        elif not data:
            break
        else:
            privatemessage += data.decode('utf-8')

    # send private message to the target user
    for c, n in client.items():
        if (n[0] == username):
            log('{0} sent a private message - \'{2}\' to {1}'.format(client[conn][0], username, privatemessage))
            c.sendall(str.encode('{0} [Private:{1}] {2}\r\n'.format(get_timestamp(), client[conn][0],privatemessage)))

# remove a user from chat room
def kick_user(conn):
    username = ''
    #conn.sendall(str.encode('\r\nEnter the user name you want to kick: '))
    while True:
        data = conn.recv(4048)
        if '\r\n' in data.decode('utf-8'):
            break
        elif not data:
            break
        else:
            username += data.decode('utf-8')

    for c, n in client.items():
        if(n[0]==username):
            c.close()  # close the kicked the connection
            del client[c] # remove the kicked user from the active client list
            return username

# leave chat room
def leave_chat_room(conn):
    name = client[conn][0]
    newadmin = make_new_admin_if_required(conn) # make new admin if existing admin left the chat room
    broadcast('\r{0} [Server] \'{1}\' left the chat room.\r\n'.format(get_timestamp(),name))
    if newadmin:#!='' or newadmin != None:
        broadcast('\r{1} [Server] \'{0}\' is the new admin.\r\n'.format(newadmin,get_timestamp()))
    del client[conn] # remove the leaving user from the active client list
    conn.close()

# make first user admin and make a new one if first one disconnects
# maintain the dictionary for chat room joining order
def make_new_admin_if_required(conn):
    newadmin=''
    if client[conn][3] == True:
        for c, n in client.items():
            if client[c] != client[conn]:
                client[c][3] = True
                newadmin = client[c][0]
                return newadmin
    return 0

# get online users information
def get_online_users():
    response = '\r\n Following users are online, Total:{0}\r\n'.format(len(client))
    table = ''
    table += '\r{0}{1}{2}\r\n'.format('IPADDRESS:PORT'.center(20), 'NAME'.center(20), 'ADMIN'.center(20))

    for c, n in client.items():
        table += '\r{1}{0}{2}\r\n'.format(str('\''+n[0]+'\'').center(20), str(n[1]+":"+n[2]).center(20), str(n[3]).center(20))

    response += table + '\r\n'
    return response

# log activity on
def log(string):
    print("[Log]",string)

# client function
def threaded_client(conn, ipaddress, port, admin):
    while True:
        name = ""
        conn.sendall(str.encode('Enter your name: '))
        while True:
            nameData = conn.recv(4048)
            if '\r\n' in nameData.decode('utf-8'):
                break
            elif not nameData:
                break
            else:
                name += nameData.decode('utf-8')

        if check_if_username_exist(name):
            conn.sendall(str.encode('Username \'{0}\' is already taken, try another name.\r\n'.format(name)))
        else:
            client[conn][0]=name
            break

    conn.sendall(str.encode('{1} [Server] Hi \'{0}\', Welcome to the chat room!\r\n{1} [Server] Type **help to get HELP information\r\n'.format(name,get_timestamp())))

    if admin:
        conn.sendall(str.encode('{0} [Server] You are the first person to join the chat room.\r\n{0} [Server] First person becomes the chat room admin by default.\r\n'.format(get_timestamp())))

    broadcast_except_sender('\r{1} [Server] \'{0}\' joined the chat.\r\n'.format(name,get_timestamp()), conn)

    reply = ""
    while True:
        data = conn.recv(4048)
        reply += data.decode('utf-8')
        if '\n' in data.decode('utf-8'): # to listen carriage return
            if len(reply) <= 2 and data == b'\r\n': # to filter-out broadcasting empty string replies when enter is pressed
                reply = ""
            else:
                reply = "{2} [{0}] {1}".format(name,reply,get_timestamp())
                broadcast_except_sender(reply, conn)
                reply = ""
        elif '\b' in data.decode('utf-8'): # for backspace deletion
            reply = reply[0:len(reply) - 2]

        # Liteners for commands typed in telnet client
        if reply=='**help':
            conn.sendall(str.encode(helpmessage))
            reply = ""
        elif reply=='**users':
            conn.sendall(str.encode(get_online_users()))
            reply = ""
        elif reply == '**kick:' and client[conn][3] == True:
            kickeduser = kick_user(conn)
            log('kicked user:',kickeduser)
            if kickeduser:
                message = '\r\n{0} [Server] \'{1}\' was kicked out of the chat room by Admin[{2}] \r\n'.format(get_timestamp(),kickeduser,get_chat_room_admin())
                log('\'{0}\' was kicked out of the chat room by Admin[{1}] \r\n'.format(kickeduser,get_chat_room_admin()))
                broadcast(message)
            reply = ""
        elif reply=='**kick:' and client[conn][3]==False:
            conn.sendall(str.encode('\r\nOnly admins can kick others users out of the chat room.\r\nTo check who is administrator type \'**users\'\r\n'))
            reply = ""
        elif reply=='**leave':
            leave_chat_room(conn)
            reply = ""
        elif reply=='**poke:':
            poke(conn)
            reply = ""
        elif reply=='**private:':
            send_private_message(conn)
            reply = ""
        elif reply=='**whoami':
            conn.sendall(str.encode('\r\n'+client[conn][0]+'\r\n'))
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
  **help             - Get Help information\r
  **users            - Get number of people online\r
  **private:username - Send a private one-to-one message (not a broadcast) to a client\r
  **kick:username    - Chat room admin's can remove people from the chat\r
  **poke:username    - Poke a person privately\r
  **leave            - To leave the chat room and close the conection\r
  **whoami           - To check your name\r
 ----------------------------------------------------------\r
'''

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)

log('Waiting for a connection.')
client = {}
usercount = 0
while True:
    conn, addr = s.accept()
    usercount+=1
    ipaddress = addr[0]
    port = str(addr[1])
    if usercount==1:
        admin = True
        client[conn]=['',ipaddress,port,admin]
    else:
        admin = False
        client[conn]=['',ipaddress,port,admin]
    log('connected to: '+addr[0]+':'+str(addr[1]))
    start_new_thread(threaded_client,(conn,ipaddress,port,admin)) # start_new_thread (function, args[, kwargs])
