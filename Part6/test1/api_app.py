# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:27:40 2021

@author: 86182
"""

from flask import Flask
 
from flask_restful import Api,Resource
 
app = Flask(__name__)
 
# 实例化一个 Api 对象，用来创建、管理 RESTful Api
api = Api(app)
 
 
# 准备一个列表数据
#datas = [{'id': 1, 'name': 'xag', 'age': 18}, {'id': 2, 'name': 'xingag', 'age': 19}]