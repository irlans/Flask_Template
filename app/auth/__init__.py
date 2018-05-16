# -*- coding:utf-8 -*-
from flask import Blueprint

# 创建蓝图路由，自定义模块路由
auth = Blueprint('auth', __name__)

from . import views
