# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:13:12 2021

@author: 86182
"""

#客户端
import socket
s = socket.socket()
host = socket.gethostname()
port = 20
s.connect((host, port))     #客户端接入
while True:
    
    mes = str(s.recv(1024),encoding = "utf-8")
    print("服务器：{}".format(mes))
    mes=(input("客户端输入的学号："))
    s.send(bytes(mes,encoding="utf-8"))
    mes=(input("客户端输入的姓名："))
    s.send(bytes(mes,encoding="utf-8"))
    mes=(input("客户端输入的成绩："))
    s.send(bytes(mes,encoding="utf-8"))
    mes=(input("客户端输入的性别："))
    s.send(bytes(mes,encoding="utf-8"))
    #mes =mes1 + mes2
    #mes3=input("客户端输入的成绩：")
    #mes4=input("客户端输入的性别：")
    #s.send(bytes(mes,encoding="utf-8"))
s.close()