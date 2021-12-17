# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:31:17 2021

@author: 86182
"""
#将时间转化为时间戳，然后将时间戳进行比较选出满足条件的列表，以数组形式返回满足条件的所有列表
import time
import numpy as np
def selectdata(init_data):
    lower = input("请输入格式如2016-05-05 20:28:54的下限时间：")
    upper = input("请输入格式如2016-05-05 20:28:54的上限时间：")

    #转换成时间数组
    uppertimeArray = time.strptime(upper, "%Y-%m-%d %H:%M:%S")
    lowertimeArray = time.strptime(lower, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    uppertimestamp = time.mktime(uppertimeArray)
    lowertimestamp = time.mktime(lowertimeArray)
    querydata=np.zeros([1,3])
    uquerydata=np.zeros([1,3])
    for i in range(3):
        n=init_data[i]
        if lowertimestamp < float(init_data[i,1]) <= uppertimestamp:
            querydata=np.row_stack([querydata,n])
        else:       
            uquerydata=np.row_stack([uquerydata,n])
            
    return querydata[1:]
