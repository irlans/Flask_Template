# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    #参数设置，可封装为config文件
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['DEBUG'] = True

    db.init_app(app)

    from app.auth import auth
    app.register_blueprint(auth)

    return app

