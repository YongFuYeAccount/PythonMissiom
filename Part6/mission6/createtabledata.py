# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:42:28 2021

@author: 86182
"""

import time
from random import randint
import Insertdata as ID

#取当前10位时间戳，返回时间戳和时间显示为列表
time_stamp = []
Datatime = []

d=['ANN人工神经网络','BP反向传播','CV计算机视觉','BN批标准化','CNN卷积神经网络',
   'DenseNet密集的CNN','DL深度学习','GPU图形处理单元','ReLU整流线性单元',
   'MLP多层感知器','LSTM长短时记忆','SGD随机梯度下降','DANN域对抗神经网络',
   'TDNN时延神经网络','WRN宽度残差网络','PAD代理距离','ABR自适应比特率算法',
   'ART自适应谐波理论','AEM自动编码机','SVM支持向量机','BMA贝叶斯平均','Bi-RNN双向循环bp']
for i in range(len(d)):
    a = int(time.time())
    b=1*randint(10,50)*55*randint(26,43)*919-1*randint(10,33)*440*randint(4,33)*818
    time_stamp.append(a+b)
    c=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a+b))
    Datatime.append(c)
#print(time_stamp,Datatime)
for i in range(len(d)):
    data=[]
    data.append(d[i])
    data.append(str(time_stamp[i]))
    data.append(Datatime[i])
    ID.Insertdata(data)
    print(data)
