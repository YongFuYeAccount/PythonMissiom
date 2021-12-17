# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:23:01 2021

@author: 86182
"""
#第一个python restful
from flask import Flask, jsonify

app = Flask(__name__)
#
test = [
    {
        'id': 1,
        'title': u'json串 1',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'json串 2',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/', methods=['GET'])#'/'里面的路径去掉可以解决404  the URL rule as string 
def get_test():
    return jsonify({'test': test})#返回上面设置的列表test


if __name__ == '__main__':
    # make jsonify support chinese
    app.config['JSON_AS_ASCII'] = False  # 否则在web端显示的是utf-8的编码，而不是中文（但是不影响接口的读取）
  
    #user_bp1 = Blueprint('user',__name__,url_prefix='/user') 
    app.run(debug=True)

