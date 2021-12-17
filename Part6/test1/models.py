# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:08:46 2021

@author: 86182
"""

# models.py
import flask
#from exts import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Foo(db.Model):
    """
    模型，将映射到数据库表中
    """
    __tablename__ = 'foo'

    # 主键ID
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    # 名字
    name = db.Column(db.String(100), nullable=False)
    # 年龄
    age = db.Column(db.INTEGER)