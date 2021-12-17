# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:15:59 2021

@author: 86182
"""

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
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


@app.route('/Desktop', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    # make jsonify support chinese
    app.config['JSON_AS_ASCII'] = False  # 否则在web端显示的是utf-8的编码，而不是中文（但是不影响接口的读取）
    app.run(port=4000,debug=True)
    #app.run(host='0.0.0.0', port=8000, debug=None)

