# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:48:59 2021

@author: 86182
"""

# 查询数据
import pymysql
import numpy as np
# 连接数据库
def queryfunction():
    conn = pymysql.connect(
        host='localhost',#地址
        user='root',#用户名
        passwd='yyf314989',#密码
        port=3306,#数据库的端口号
        db='mydb_three',#数据库的名称
        charset='utf8'
        )

# 创建一个游标
    cursor = conn.cursor()
    
# 查询数据
    sql = "select * from task6"#选择列表为student
    cursor.execute(sql)  # 执行sql
# 查询所有数据，返回结果默认以元组形式，所以可以进行迭代处理

    data=np.zeros([1,3])#定义一个空矩阵
    for i in cursor.fetchall():
        a=list(i)#将查询回的元组转化为列表
        data=np.row_stack([data,a])#将每行数据保存为数组的一行
        
        #print(list(i))
    #print('共查询到：', cursor.rowcount, '条数据。')
    counts=cursor.rowcount-1
    return data[1:],counts#返回所有的数据





