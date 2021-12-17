# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:55:56 2021

@author: 86182
"""

from flask import make_response,Flask

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({'error': 'Sorry,Did not find the resources you want to visit.'}), 404)
