# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:12:26 2021

@author: 86182
"""

from flask_restful import Api,Resource
from flask import Flask
 
app = Flask(__name__)
 
# 实例化一个 Api 对象，用来创建、管理 RESTful Api
api = Api(app)
 
 
# 准备一个列表数据
datas = [{'id': 1, 'name': 'xag', 'age': 18}, {'id': 2, 'name': 'xingag', 'age': 19}]


class UserView(Resource):
    """
    通过继承 Resource 来实现调用 GET/POST 等动作方法
    """
    def get(self):
        """
        GET 请求
        :return:
        """
        return {'code': 200, 'msg': 'success', 'data': datas}
 
 
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
api.add_resource(UserView,'/user') #通过继承 Resource 来实现调用 GET/POST 等动作方法
if __name__ == '__main__':
    app.run()  
    
    
    
    
    