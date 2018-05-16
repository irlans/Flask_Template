# -*- coding:utf-8 -*-
from app import db

class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String)
    def __repr__(self):
        return '<User %r>' % self.username