# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:42:55 2021

@author: 86182
"""

#输入部分
inputstr=input("输入任意的数字、大小写字母、符号：\n")
ascii_codes=[] # set an empty list to contain ASCII codes

#求出输入字符串中的各个字符对应的ASCII码值，用ord函数取出ASCII值，用append（）函数将各个ASCII码值插入到list后面
for i in range(len(inputstr)): #len 求出输入字符串的长度
    ascii_codes.append(ord(inputstr[i])) 
      
# printing the result    
print('The ASCII value of each character are:',ascii_codes)

#对ASCII码升序排序
ascii_codes.sort() 

#创建空列表放置数字，大小写字母和符号
number=[]
upperletter=[]
lowerletter=[]
signal=[]

#将ASCII码分为四类，按照ASCII码表的对应值
for i in range(len(inputstr)):
    if 47 < ascii_codes[i] <=57:
        number.append(ascii_codes[i])#将符合条件的ASCII码插入到对应列表的最后
    elif 64 < ascii_codes[i] <=90:
        upperletter.append(ascii_codes[i])
    elif 96 < ascii_codes[i] <=122:
        lowerletter.append(ascii_codes[i])
    else:
        signal.append(ascii_codes[i])
        
 #将多个list合为一个过度列表      
middle=number+upperletter+lowerletter+signal

#将ASCII码转化为对应的字符 
output=[]
for i in range(len(middle)):
    output.append(chr(middle[i])) 

#先把列表中的所有元素转化为字符
list2 = [str(i) for i in output]

#print(list2)
#使用join的方法将列表list2转化为字符串
str1 = ''.join(list2)

#输出
print('输入字符串中的数字个数：',len(number))
print('输入字符串中的大写字母个数：',len(upperletter))
print('输入字符串中的小写字母个数：',len(lowerletter))
print('输入字符串中的符号个数：',len(signal))
#print('按照要求排序后的字符串list：',output)
print('输入的字符串：',inputstr)
print('按要求排序后输出的字符串：',str1)


   




                


    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        