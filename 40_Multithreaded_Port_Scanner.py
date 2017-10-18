import threading
from queue import Queue
import socket
import time

printlock = threading.Lock()  # perform a thread lock
server = 'geekeefy.wordpress.com'

# The actual job that is multi-threaded
def scanport(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = s.connect((server, port))
        with printlock:
            print('Port:',port,'is OPEN')
        connection.close()
    except:
        pass
        #print('Port:',port,'is CLOSED')

def threader():
    while True:
        worker = q.get()  # .get() fetches a item (port no. here) from the queue
        scanport(worker)  # actual job
        q.task_done()  # indication that task was complete


q = Queue()  # create a queue. The Queue module allows you to create a new queue object that can hold a specific number of items.

for x in range(1000): # number of parallel threads
    t = threading.Thread(target=threader)  # defining the thread and its target
    t.daemon = True  #
    t.start()  # start the thread

starttime = time.time()

for worker in range(1,1025):
    q.put(worker)  # adding items to the queue

q.join()  # blocks untill all items of the queue are returned and processed

print('entire job took:', time.time() - starttime, 'seconds')
