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
                         database="mydb_one")
    print('连接上了!')
    return db

def createtable(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # 如果存在表task4先删除
    cursor.execute("DROP TABLE IF EXISTS Task4")
    sql = """CREATE TABLE Task4 (
            sno CHAR(20),
            sname CHAR (20),
            score CHAR (20),
            sex CHAR (20),
            ID CHAR(20) ,
            host CHAR(20) ,
            timestamp CHAR(30),
            datatime CHAR(30) )"""

    
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