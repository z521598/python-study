#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

'''
socket server
'''

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)

while True:
    c , addr = s.accept()
    c.send("hello,client")
    print "client address:",addr
    c.close()


