#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import threading
from threading import Thread;

import thread


class Counter(Thread):
    'counter'
    count = 0;
    lock = thread.allocate_lock();

    def __init__(self,slock):
        Thread.__init__(self);
        self.slock = slock;

    def run(self):
        # Counter.lock.acquire();
        print "in:",self.slock.locked();
        self.slock.acquire();
        for i in range(1000):
            Counter.count += 1;
            # print Counter.count;
        print "out:",self.slock.locked();
        self.slock.release();
        # Counter.lock.release();