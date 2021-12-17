# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:59:24 2021

@author: 86182
"""

# config.py
USERNAME = 'root'
PASSWORD = 'yyf314989'
HOSTNAME = "127.0.0.1"
PORT = '3306'
DATABASE = 'mydb_three'

DIALECT = 'mysql'
DRIVER = 'pymysql'

# 连接数据的URI
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SWAGGER_TITLE = "API"
SWAGGER_DESC = "API接口"
# 地址，必须带上端口号
SWAGGER_HOST = "localhost:5000"