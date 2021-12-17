# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:37:30 2021

@author: 86182
"""
import time
import numpy as np
o=np.zeros(0)
a=['dann', '1462451334', '2021-10-21 10:46:14']
b=['sgd', '1462456334', '2021-10-21 11:01:14']
c=['sgd', '1463455334', '2021-10-21 11:01:14']
d=['sgd', '1872452334', '2021-10-21 11:01:14']

#f=[1,1,1,1]
o=np.array([a,b,c,d])
lower = input("请输入格式如2016-05-05 20:28:54的下限时间：")
upper = input("请输入格式如2016-05-05 20:28:54的上限时间：")

#转换成时间数组
uppertimeArray = time.strptime(upper, "%Y-%m-%d %H:%M:%S")
lowertimeArray = time.strptime(lower, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
uppertimestamp = time.mktime(uppertimeArray)
lowertimestamp = time.mktime(lowertimeArray)

t=[1,2,3]
querydata=np.zeros([1,3])
uquerydata=np.zeros([1,3])
for i in range(3):
    n=o[i]
    if lowertimestamp < float(o[i,1]) <= uppertimestamp:
        print(float(o[i,1]))
        querydata=np.row_stack([querydata,n])
    else:       
       uquerydata=np.row_stack([uquerydata,n])
print(querydata)
print(o)
print (uppertimestamp) 
print (lowertimestamp)      
 
    
 
    
 
    
 
#o=np.column_stack([d,f])
#o=np.row_stack([a])
#o=np.row_stack([o,b])
#print(o)
#u=o.tolist()
#print(o[1:])
#print(u)
#print(o[1])