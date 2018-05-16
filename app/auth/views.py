# -*- coding:utf-8 -*-
from . import auth


@auth.route("/",methods=["GET","POST"])
def index():
    return "hello!world!"