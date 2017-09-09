# !/usr/bin/env python
# *_*coding:UTF-8 *_*
# producer_consumer_queue

from Queue import Queue
import random
import threading
import time

class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self)
        self.name = name
        self.data = queue

    def run(self):
        for i in range(5):
            print "%s: %s is producing %d to the queue!\n" %(time.ctime(), self.getName(), i)
            self.data.put(i)
            time.sleep(random.randrange(5,10));
        print "%s: %s finished!" %(time.ctime(), self.getName())

