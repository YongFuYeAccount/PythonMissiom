# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:34:06 2021

@author: 86182
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
import random


plt.ion() #开启interactive mode 成功的关键函数
plt.figure(1)
t = [0]
t_now = 0
#m = [sin(t_now)]
m = [0]
c=0



for n in range(2):
    for i in range(2):
        plt.clf() #清空画布上的所有内容
        #t_now = i*0.1
        #t_now = i*1
       
        num = 0 #暂停执行程序的时间
        time.sleep(num)
        t_now=random.randint(0,20)
        t.append(t_now)#模拟数据增量流入，保存历史数据（）
            #m.append(sin(t_now))#模拟数据增量流入，保存历史数据
        c=c+1
        m.append(c)
        plt.plot(m,t,'-r')#画出红色的点
    #plt.draw()#注意此函数需要调用
    #time.sleep(0.01)
        plt.pause(1)
               
   
           
    
    
    
    
    