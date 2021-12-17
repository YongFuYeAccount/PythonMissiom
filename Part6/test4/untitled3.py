# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:07:30 2021

@author: 86182
"""
import queryfunction as qf
import Insertdata as ID

import numpy as np
#A=qf.queryfunction()
#coding:UTF-8
import time

#upper = input("请输入格式如2016-05-05 20:28:54的上限时间：")
#lower = input("请输入格式如2016-05-05 20:28:54的下限时间：")
#转换成时间数组
dt= "2016-05-05 20:28:54"
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)

print (timestamp)






