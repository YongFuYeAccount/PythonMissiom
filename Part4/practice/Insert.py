# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 12:24:01 2021

@author: 86182
"""

# 插入数据
import pymysql
import GetN as gt
# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='yyf314989',
    port=3306,
    db='mydb_two',
    charset='utf8'
)
data = []
data.append(input('输入需要传输的数据：'))
data = data+ gt.GetN()
# 创建一个游标
cursor = conn.cursor()
# 插入数据
# 数据直接写在sql后面
sql = "insert into test(data,timestamp,daytime) values(%s, %s, %s)"  # 注意是%s,不是s%
cursor.execute(sql, data)  # 列表格式数据
#cursor.execute(sql, ("00014", '马六',"24","1"))  # 元组格式数据

# 数据单独赋给一个对象
#sql = "insert into student values(%s,%s,%s, %s)"
#data = ("00015", '老七',24,0)
#cursor.execute(sql, data)  #sql和data之间以","隔开

# sql = "insert into student values(%s,'%s',%s',%s')"
# data = ("D00015", '小八',25,0)
# cursor.execute(sql % data) #sql和data之间以"%"隔开，此时它的sql中注意要给中文字符对应的占位符加上引号，即"%s",不然会报错：unsupported format character

conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
cursor.close()  # 关闭游标
conn.close()  # 关闭连接

