# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:55:59 2021

@author: 86182
"""


#取当前10位时间戳，返回时间戳和时间显示为列表
import time
import math

def GetN():
    TIME =[]
    time_stamp = int(time.time())
    TIME.append( time_stamp)
    #print(time_stamp)
    Datatime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time_stamp))
    #print(Datatime)
    TIME.append(Datatime)
    return  TIME

