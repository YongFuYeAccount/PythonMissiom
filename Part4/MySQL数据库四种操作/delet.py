# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:51:55 2021

@author: 86182
"""
# 删除数据
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

# 删除数据
sql = "delete from student where age=%s"
data = (24)
cursor.execute(sql, data)

conn.commit()   # 提交，不然删除操作不生效
cursor.close()  # 关闭游标
conn.close()  # 关闭连接

