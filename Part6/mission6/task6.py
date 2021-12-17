# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:12:26 2021

@author: 86182
"""

from flask_restful import Api,Resource
from flask import Flask
import queryfunction as qf
import numpy as np
import selectdata as sd

app = Flask(__name__)
 
# 实例化一个 Api 对象，用来创建、管理 RESTful Api
api = Api(app)
 
# 准备一个列表数据
datas,rowcounts=qf.queryfunction()#调用查询函数查出数据库中所有的数据并存在列表中
datas=sd.selectdata(datas,rowcounts)#选出满足在某时间段保存的数据
datas=datas.tolist()#将数组转化为列表
class UserView(Resource):
    """
    通过继承 Resource 来实现调用 GET/POST 等动作方法
    """
    def get(self):
        """
        GET 请求
        :return:
        """
        #return {'code': 200, 'msg': 'success', 'data': datas}
        return { 'msg': '满足时间段的数据','data': datas}
      
 
    def post(self):
        # 参数数据
        json_data = request.get_json()
 
        # 追加数据到列表中
        new_id = len(datas)+1
        datas.append({'id':new_id,**json_data})
 
        # 返回新增的最后一条数据
        return {'code': 200, 'msg': 'ok', 'success': datas[new_id - 1]}
    

# 暴露接口出去
# 资源路由：UserView
# 路径：/user
api.add_resource(UserView,r'/user') #通过继承 Resource 来实现调用 GET/POST 等动作方法
if __name__ == '__main__':      #路径和原来一样
    app.run()  
    
    
    
    
    