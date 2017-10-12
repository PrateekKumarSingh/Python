'''
threading.activeCount() − Returns the number of thread objects that are active.
threading.currentThread() − Returns the number of thread objects in the caller's thread control.
threading.enumerate() − Returns a list of all thread objects that are currently active.

In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −

run() − The run() method is the entry point for a thread.
start() − The start() method starts a thread by calling the run method.
join([time]) − The join() waits for threads to terminate.
isAlive() − The isAlive() method checks whether a thread is still executing.
getName() − The getName() method returns the name of a thread.
setName() − The setName() method sets the name of a thread.
'''

import threading
import time

exitflag = 0

# Overriding the parent class: 'threading.thread' to create a subclass 'mythread'
class mythread (threading.Thread):  
    def __init__(self, threadID, name, counter): # __init__() is the constructor to initialize the values
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    # to specify the activity the thread performs there are two ways
    # 1. overriding run() method of parent class: 'threading.thread' to define the activity
    # 2. pass a callable object to the constructor of 'threading.thread' class, like - threading.Thread(target=threader)
    def run(self): 
        print('Starting ',self.name)
        job(self.name, self.counter, 5)
        print('Exiting ',self.name)

# the actual job that the thread executes
def job(threadname, delay, counter):
    while counter:
        if exitflag:
            threadname.exit()
        time.sleep(delay)
        print("{0}: {1}".format(threadname, time.ctime(time.time())))
        counter -=1

# create new threads
thread1 = mythread(1, 'Thread-1', 1)        
thread2 = mythread(2, 'Thread-2', 2)

# start new threads
thread1.start()
thread2.start()
thread1.join() # waits until the thread terminates
thread1.join() # waits until the thread terminates

print('Exiting Main Thread')
