# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:53:57 2021

@author: 86182
"""
import socket

def SERVER1():
    s = socket.socket()
    host = socket.gethostname()
    port = 9003
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
            #mes = input("服务器：")
            #c.send(bytes(mes,encoding="utf-8"))
                
            break
        c.close()
        break 
    return mes #返回的类型是字符串（str）