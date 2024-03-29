#!usr/bin/python


import threading
import time

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
	self.threadID = threadID
	self.name = name
	self.count = count
    def run(self):
        print "starting thread " + self.name
	print_time(self.name, self.count, 5)
	print "exit thread " + self.name

def print_time(threadName, delay, counter):
    while counter:
        #if exitFlag:
            #thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print "Exiting Main Thread"
	
    

