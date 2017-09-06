#! /usr/bin/env python
# *_* coding : UTF-8 *_*

class ThreadObj2:
    'simple classtest Realization, counter function'
    count = 0;

    def __init__(self, name):
        self.name = name;
        print "i am ", name;
        ThreadObj2.count += 1;

    def setName(self,name):
        self.name = name;

    def setAge(self,age):
        self.age = age;

    @staticmethod
    def getCount():
        return ThreadObj2.count;


def printStr(str):
    print str;
