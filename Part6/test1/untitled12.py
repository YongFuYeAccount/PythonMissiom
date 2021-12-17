# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:12:40 2021

@author: 86182
"""

# 初始化迁移文件
python3 manager.py db init

# 映射到文件
python3 manager.py db migrate

# 映射到数据库
python3 manager.py db upgrade