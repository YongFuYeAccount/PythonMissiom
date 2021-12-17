# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:08:42 2021

@author: 86182
"""

import pymysql

def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:root, 密码:yyf314989，
    #并且要创建数据库mydb_one，并在数据库中创建好表
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="yyf314989",
                         database="mydb_three")
    print('连接上了!')
    return db

def createtable(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # 如果存在表test先删除
    cursor.execute("DROP TABLE IF EXISTS test1")
    sql = """CREATE TABLE test1 (
            data CHAR(20),
            timestamp CHAR(20),
            daytime CHAR(20) )"""

    
    # 创建task4表
    cursor.execute(sql)

def closedb(db):
    db.close()

def main():
    db = connectdb()    # 连接MySQL数据库

    createtable(db)     # 创建表
    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    main()