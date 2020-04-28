# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 18:57
# @Author  : guoyunfei.0603
# @File    : home_work.py

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("第一个用户：",self.first_name)
        print("第二个用户:",self.last_name)

    def greet_user(self):
        print("你好啊")
        self.describe_user()

user = User("天一","天二")
# user = User("阿贵","阿宝")
# user = User("吱吱","乐乐")
g = user.greet_user()
print(g)

