# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:53:06 2021

@author: 86182
"""
#按照行输出
l=["A","B","C","D"]
f=open("k1.txt","w")
f.writelines(l)
f.close()# 输出样式：ABCD

#输出为列表
l=["A","B","C","D",1,2,3]
f=open("k2.txt","w")
f.write(str(l))
f.close()# 输出样式：['A', 'B', 'C', 'D', 1, 2, 3]

#每个元素为一行
l=["A","B","C","D"]
str = '\n'
f=open("k3.txt","w")
f.write(str.join(l))
f.close()
'''
输出样式：
A
B
C
D
'''
