# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:28:28 2021

@author: 86182
"""

#定时一秒显示随机数
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
import random


plt.ion() #开启interactive mode 成功的关键函数
plt.figure(1)#图名figure1 
t = [0]
#t_now = 0
#m = [sin(t_now)]
m = [0]
c=0 #第零次

for i in range(5):#动态显示五个数
    plt.clf() #清空画布上的所有内容
    #t_now = i*0.1
    #t_now = i*1
    while True:
        num = 0 #暂停执行程序的时间
        time.sleep(num)
        t_now=random.randint(0,20)#产生0——20的随机数 
        t.append(t_now)#模拟数据增量流入，保存历史数据（）
        #m.append(sin(t_now))#模拟数据增量流入，保存历史数据
        c=c+1#每次加一
        m.append(c)
        plt.plot(t,m,'-r')#画出红色的点
    #plt.draw()#注意此函数需要调用
    #time.sleep(0.01)
        plt.pause(1)
        break 
    
    
    
    
    
    
    
    
    
    
    