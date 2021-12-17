# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:20:01 2021

@author: 86182
"""
#服务器端
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
import random
import socket

s = socket.socket()
host = socket.gethostname()
port = 9 #连接的端口号需要和服务器端一致
s.bind((host, port)) #服务器端套接字. s.bind () 绑定地址（host,port）到套接字， 在 AF_INET下，以元组（host,port）的形式表示地址。

plt.ion() #开启interactive mode 成功的关键函数
plt.figure(1)
t = [0]
m = [0]
storage=[]



s.listen(5)
while True:
    print('等待用户连接……')
    c, addr = s.accept()        #阻塞进程，等待客户端接入
    print('用户已连接 address:{}\n服务器:请问需要什么帮助'.format(addr))
    c.send(bytes("请发送数据：",encoding="utf-8"))
    while True:
        
        for i in range(20):#动态显示二十个数
            mes = str(c.recv(1024),encoding = "utf-8")
            print("客户端：{}".format(mes))
            storage.append(mes)#储存接收到的所有数据
            plt.clf() #清空画布上的所有内容
            time.sleep(0)#时间中断0秒
            t.append(mes)#模拟数据增量流入，保存历史数据（）
            m.append(i)#
            plt.plot(m,t,'-r')#画出红色的线
            plt.pause(1)#画图停止1秒               
            mes='next'#发送给客户端
            c.send(bytes(mes,encoding="utf-8"))#实现发送随机数给客户端
        break       
    c.close()
    break
print('动态显示完成，已拒绝接收数据') 







