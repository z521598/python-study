# !/usr/bin/env python
# *_*coding:UTF-8 *_*
import threading
import random
import time


class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)

        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()

            print "%s: %s is consuming. %d in the queue is consumed!\n" % (time.ctime(), self.getName(), val)

            time.sleep(random.randrange(10))

        print "%s: %s finished!" % (time.ctime(), self.getName())
