# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:48:36 2021

@author: 86182
"""

python3 manage.py db stamp head 
# 初始化迁移文件
python3 manager.py db init
 
# 映射到文件
python3 manager.py db migrate
 
# 映射到数据库
python3 manager.py db upgrade