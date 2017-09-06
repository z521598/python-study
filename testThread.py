#! /usr/bin/env python
#  _*_ coding:UTF-8 _*_
import thread

import time;


def print_time(delay, sum=5):
    print "start";
    for i in range(sum):
        time.sleep(delay);
        print time.time();
    else:
        print "end";


thread.start_new_thread(print_time, (1,));
thread.start_new_thread(print_time, (2,));

time.sleep(9)