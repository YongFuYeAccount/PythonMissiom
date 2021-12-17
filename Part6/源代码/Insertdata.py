# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:46:11 2021

@author: 86182
"""

# 插入数据
import pymysql
# 连接数据库
def Insertdata(data): 
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='yyf314989',
        port=3306,
        db='mydb_three',
        charset='utf8')
    # 创建一个游标
    cursor = conn.cursor()
# 数据直接写在sql后面
    sql = "insert into task4(sno,sname,score,sex,ID,host,timestamp,datatime) values( %s, %s, %s, %s,%s, %s, %s, %s)"  # 注意是%s,不是s%
    #sql = "insert into student(sno,sname,grade,sex) values(%s, %s, %s, %s)"
    cursor.execute(sql, data)  # 列表格式数据
    conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接