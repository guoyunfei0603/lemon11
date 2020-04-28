# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 20:12
# @Author  : guoyunfei.0603
# @File    : class_object2.py

class Login:
    def __init__(self,session):
        if session == None:
            print("跳转到登录页")
        else:
            print("跳转到首页")
            self.index()

    def index(self):
        print("跳转到首页成功")

session = "ewyyudwbwu32ieyu2gyu2"
# __init__ 初始化的时候就必须写对应的属性值
g = Login(session)



# 如果没有__init__
class Register:
    def user(self,uname,uid):
        print(uname,uid)

r = Register()
r.user("同科",12311)

