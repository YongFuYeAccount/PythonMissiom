# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:49:55 2021

@author: 86182
"""
# 修改数据
import pymysql

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='yyf314989',
    port=3306,
    db='mydb_one',
    charset='utf8'
)

# 创建一个游标
cursor = conn.cursor()
# 修改数据
sql = "update student set sname='%s' where age=%s"  #注意%s什么时候加引号，什么时候不加
data = ('mydb_one)', 24)
cursor.execute(sql % data)



conn.commit()   # 提交，不然无法保存插入或者修改的数据

cursor.close()  # 关闭游标
conn.close()  # 关闭连接

