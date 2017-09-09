# !/usr/bin/env python
# *_*coding:UTF-8 *_*
import threading
import random
import time
import Queue
from Producer import Producer
from Consumer import Consumer

queue = Queue.Queue();
queue = Queue.Queue();

producer = Producer("pro", queue);
consumer = Consumer("con", queue);

producer.start()

consumer.start()

producer.join()

consumer.join()

print 'All threads terminate!'
