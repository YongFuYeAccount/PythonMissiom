# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:14:49 2021

@author: 86182
"""
#服务器
import GetN as gt
import socket
import Insertdata as Idata
import pymysql
import queryfunction as qf

s = socket.socket()
host = socket.gethostname()
port = 206
s.bind((host, port))

s.listen(5)
while True: # 循环锁定访问客户端
    print('等待用户连接……')
    c, addr = s.accept()        #阻塞进程，等待客户端接入 # 返回链接的标记位conn，与连接的地址
    print('用户已连接 address:{}\n服务器:请问需要什么帮助'.format(addr))#format函数把元组转化为字符串
    c.send(bytes("请问需要什么帮助?",encoding="utf-8"))
    while True:
        totaldata = []#待存储进数据库的数据
                 #存放地址和端口号
       
        mes = str(c.recv(1024),encoding = "utf-8")#接收客户端发来的信息 
        #.接收数据,默认1024字节，缓冲区每次最多发32768，
        #每个系统不同，超出数值会有限制。字节如果发不完会存在缓冲去，下次在发送
        
        totaldata.append(mes) #将学号信息插入数据list
        print('学生学号为',mes)
        
        mes = str(c.recv(1024),encoding = "utf-8")#接收客户端发来的信息
        totaldata.append(mes) #将姓名信息插入数据list
        print('学生姓名为',mes)
        
        mes = str(c.recv(1024),encoding = "utf-8")#接收客户端发来的信息
        totaldata.append(mes) #将姓名信息插入数据list
        print('学生成绩为',mes)
        
        mes = str(c.recv(1024),encoding = "utf-8")#接收客户端发来的信息
        totaldata.append(mes) #将姓名信息插入数据list
        print('学生性别为',mes)
        print('学生总的信息列表',totaldata)
        
        #c, addr = s.accept()    #阻塞进程，等待客户端接入
        adddata=list(addr) #将地址和端口号转存到adddata list中
        adddata[-1]=str(adddata[-1])#将int转化为str
        
        
        d=gt.GetN()#将时间戳和时间保存到d列表中
        d[0]=str(d[0])
        totaldata= totaldata + adddata + d #将所有数据合并到一list中
        
        print(totaldata)
        
        Idata.Insertdata(totaldata)#调用函数插入数据
        #print("客户端：{}".format(mes))
        #print('此时的时间戳',d)
        #print('此客户端的地址和断口号',adddata)
        print('全部信息',totaldata)
        qf.queryfunction()#查询数据库
        mes = input("服务器：")
        c.send(bytes(mes,encoding="utf-8"))
        
    c.close()
