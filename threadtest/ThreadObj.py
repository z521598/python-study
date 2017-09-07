#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import threading;
from threading import Thread;
import time


class ThreadObj(Thread):
    'thread simple Realization'
    count = 0;

    def __init__(self,delay):
        threading.Thread.__init__(self);
        self.delay = delay;

    def run(self):
        for i in range(8):
            time.sleep(self.delay);
            print Thread.getName(self);
