# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:12:07 2021

@author: 86182
"""

# manager.py
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from exts import db
from api_app import app
from models import Foo

manager = Manager(app)
migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()