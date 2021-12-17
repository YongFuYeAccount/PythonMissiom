# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:03:16 2021

@author: 86182
"""
import random
import time
import socket

while True:
    s = socket.socket()
    host = socket.gethostname()
    port = 9
    s.connect((host, port))     #客户端接入
    while True:
        mes = str(s.recv(1024),encoding = "utf-8")
        print("服务器：{}".format(mes))#实现能够接收来自客户端的随机数
        #mes = input("客户端：")
        while True:
            num = 1 #暂停执行程序的时间
            time.sleep(num)
            mes = random.randint(0,20)
            mes =str(mes)
            s.send(bytes(mes,encoding="utf-8"))
            #s.send(mes)
    s.close()

