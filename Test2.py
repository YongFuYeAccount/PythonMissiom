# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:42:06 2021

@author: 86182
"""

from os.path import join, getsize
from os import listdir
import pandas as pd
import os
import time
import math

#定义读取文件夹里文件名的文件函数
def getlist(Filename):
    FileList = listdir(Filename) 
    return FileList

#输入部分，得到目标文件夹下所有文件名的list
Input=input("请输入目标文件夹：\n")
filename=getlist(Input)


#读取文件的类型
filetype = []
for i in range(len(filename)):
    filetype.append(((filename[i])[(filename[i]).rfind("."):])[1:])
    
#读取文件名的字符串的前缀(不带后缀的文件名)
filestr = []
for i in range(len(filename)):
    filestr.append((filename[i]).split('.')[0])
    
    
#读取各种文件类型的数量
dict1={}
for list in filetype:
    keys=list.split(" ")
    for key in keys:
        if key in dict1.keys():
            dict1[key]=dict1[key]+1
        else:
            dict1[key]=1
    
    
#定义一个空list存放文件大小,
#批量读取对应文件夹里所有文件的大小
filesize = []
for i in range(len(filename)):
    filenamestr = filename[i]
    filesize.append(int((os.path.getsize(join(Input,filenamestr)))/1024))#append函数直接在空list里可以插入值，join函数用于找出要读取的文件名称
    #将字节转化为kb
    
    
#创建个空list存放创建、访问、修改时间
#批量读取对应文件夹里所有文件的创建时间戳
filectime = []
fileatime = []
filemtime = []
for i in range(len(filename)):
    filenamestr = filename[i]
    filectime.append(os.path.getctime(join(Input,filenamestr)))#getctime 创建时间、getatime 访问时间 、getmtime更改时间
    fileatime.append(os.path.getatime(join(Input,filenamestr)))
    filemtime.append(os.path.getmtime(join(Input,filenamestr)))
    


#创建一个存放单位精确到s的list
#将filetime里的时间保留到秒，即去掉小数
filectimes=[]
fileatimes=[]
filemtimes=[]
for i in range(len(filectime)):
    filectimes.append(math.floor(filectime[i]))
    fileatimes.append(math.floor(fileatime[i]))
    filemtimes.append(math.floor(filemtime[i]))



#将创建时间戳转化为具体时间
realctime = []
realatime = []
realmtime = []
timecArray=[]
timeaArray=[]
timemArray=[]
for i in range(len(filectimes)):
    timecStamp=filectimes[i]
    timecArray.append(time.localtime(timecStamp))
    realctime.append(time.strftime("%Y-%m-%d %H:%M:%S", timecArray[i]))
    
    timeaStamp=fileatimes[i]
    timeaArray.append(time.localtime(timeaStamp))
    realatime.append(time.strftime("%Y-%m-%d %H:%M:%S", timeaArray[i]))
    
    timemStamp=filemtimes[i]
    timemArray.append(time.localtime(timemStamp))
    realmtime.append(time.strftime("%Y-%m-%d %H:%M:%S", timemArray[i]))
    

#字典中的key值即为csv中列名
dataframe = pd.DataFrame({"文件名       ":filestr,
                          "文件尺寸(KB)  ":filesize,
                          "文件类型      ":filetype,
                          "文件创建时间   ":realctime,
                          "文件访问时间   ":realatime,
                          "文件修改时间   ":realmtime})

#将DataFrame存储为csv,index表示是否显示行名，default=True 分隔符选用分号
dataframe.to_csv(r"SummaryIformation.csv",index=False,sep=';')


#输出部分
#print('文件夹下所有文件的全称list：',filename)
#print('不带文件后缀的文件名',filestr)
#print("文件类型：",filetype)  
#print('得到的文件尺寸list(KB)：',filesize)
print('各个文件及其对应的大小(名称：大小（KB）)：',dict(zip(filestr,filesize)))
print("各种类型文件的数量：",dict1)
print('文件夹里所有文件的大小和(KB)：',sum(filesize))    
#print('得到的文件创建时间list：',filectime)    
#print('精确度保留到秒的时间戳：',filectimes,fileatimes,filemtimes)
#print('得到的文件实际创建时间list：',realctime)
#print('得到的文件实际访问时间list：',realatime)
#print('得到的文件实际修改时间list：',realmtime)
print("文件夹中所有文件的名称、大小，类型、文件创建时间等基本信息，保存到了SummaryIformation.csv文件中")










