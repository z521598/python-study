#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import time;
import calendar

print "你好，python";
print time.time();
t = time.localtime(time.time());
print time.asctime(t);

ti = time.time();
print calendar.month(2017,1);
print calendar.month(t.tm_year,t.tm_mon)
