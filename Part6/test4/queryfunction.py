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
      #  print(i)
        a=list(i)
        data=np.row_stack([data,a])
     #   print(list(i))
    #print('共查询到：', cursor.rowcount, '条数据。')
    return data[1:]#返回所有的数据





