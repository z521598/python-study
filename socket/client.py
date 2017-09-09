#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

'''
socket client
'''

import socket

sc = socket.socket();
host = socket.gethostname()
port = 12345
sc.connect((host,port))

print sc.recv(1024);

sc.close();