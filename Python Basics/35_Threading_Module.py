import threading
from queue import Queue
import time

printlock = threading.Lock() # perform a thread lock

# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        worker = q.get() # .get() fetches a item from the queue
        time.sleep(0.5)
        with printlock:
            print(threading.current_thread().name, worker)
        q.task_done() # indication that task was complete

q = Queue() # create a queue. The Queue module allows you to create a new queue object that can hold a specific number of items.

# number of thread we want to allow to run in parallel
for x in range(10):
    t = threading.Thread(target=threader) # defining the thread and its target
    t.daemon = True  # classifying this thread as a daemon, so they will die when the main thread dies
    t.start() # start the thread, must come after daemon definition

start = time.time() # noting the start time

# put jobs in a queue, from where a thread can pick it
for worker in range(20):
    q.put(worker) # adding items to the queue

q.join() # blocks/waits until all items of the queue are returned and processed

print('entire job took:', time.time()-start)
