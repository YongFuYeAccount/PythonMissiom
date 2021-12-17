# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:21:56 2021

@author: 86182
"""
#将list中的元素依次写入txt中(包含此时刻的时间)
import GetN as gt
def WDataLIST(data):
    data=data + gt.GetN()
    f=open("k1.txt","a")#打开文本，追加数据
    f.writelines('\n')#每次追加数据时换行
    for i in range(len(data)):
        data[i] = str(data[i])#将列表中的数据全部转化为字符串
        f.write(data[i])
        f.write(',')#列表中的数据全部以‘，’分割开
    
    
    #f.writelines(str(data))#把data以字符串形式写入
    f.close()# 输出样式：ABCD
    
    




