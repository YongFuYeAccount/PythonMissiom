# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:07:06 2021

@author: 86182
"""
#demo_2:传参
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:test_id>', methods=['GET'])
def get_test(test_id):
    #task = list(filter(lambda t: t['id'] == task_id, tasks))
    task = list(filter(lambda t: t['id'] == test_id, tests))#
    if len(test) == 0:
        abort(404)
    return jsonify({'task':test[0]})


if __name__ == '__main__':
    # make jsonify support chinese
    app.config['JSON_AS_ASCII'] = False  # 否则在web端显示的是utf-8的编码，而不是中文（但是不影响接口的读取）
    app.run(debug=True)
