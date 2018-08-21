#coding:utf8

from  flask import  Flask

app = Flask(__name__)
app.debug = True

from  app.home import  home as home_blueprint
from  app.admin import  admin as admin_blueprint
from  app.api import  api as api_blueprint
from  app.api2 import  api2 as api2_blueprint

# app  注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(api_blueprint, url_prefix="/api")
app.register_blueprint(api2_blueprint, url_prefix="/api2")
