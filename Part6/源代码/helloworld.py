# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:11:10 2021

@author: 86182
"""

from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def hello_world():
    return 'Hello World!'
 
 
if __name__ == '__main__':
    app.run()