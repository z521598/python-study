# !/usr/bin/env python
# *_*coding:UTF-8 *_*
import time;
import Queue;
import threading;

q = Queue.Queue();
for i in range(9):
    q.put(i);

while not q.empty():
    print q.get();

