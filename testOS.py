#! /usr/bin/env python
# _*_ coding:UTF-8 _*_
import os;
import sys;

print os.getuid();
res=os.system("ls -al");

print "******************"
print res;
