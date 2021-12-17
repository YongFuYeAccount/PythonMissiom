# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:39:43 2021

@author: 86182
"""

#服务器端
import socket
s = socket.socket()
host = socket.gethostname()
port = 9000
s.bind((host, port))

s.listen(5)
while True:
    print('等待用户连接……')
    c, addr = s.accept()        #阻塞进程，等待客户端接入
    print('用户已连接 address:{}\n服务器:请发送数据'.format(addr))
    c.send(bytes("请问需要什么帮助?",encoding="utf-8"))
    while True:
        mes = str(c.recv(1024),encoding = "utf-8")
        print("客户端：{}".format(mes))
        mes = input("服务器：")
        c.send(bytes(mes,encoding="utf-8"))

    c.close()


