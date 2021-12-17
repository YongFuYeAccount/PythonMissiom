# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:40:22 2021

@author: 86182
"""

import socket
s = socket.socket()
host = socket.gethostname()
port = 9044
s.connect((host, port))     #客户端接入
while True:
    mes = str(s.recv(1024),encoding = "utf-8")
    print("服务器：{}".format(mes))
    mes = input("客户端：")
    s.send(bytes(mes,encoding="utf-8"))
s.close()

