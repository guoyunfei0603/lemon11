# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 15:32
# @Author  : guoyunfei.0603
# @File    : class_object3.py
"""
1. 当你想调用静态属性的时候用cls
2. 当你写的方法想让别人调用的时候用静态函数
"""

class Teacher:
    name = "~~我是静态属性~~"

    def __init__(self):
        print("我是初始化方法")

    @classmethod
    def class_test(cls):
        print("我是类方法"+cls.name)

    @staticmethod
    def static():
        print("我是静态方法")

    def common(self):
        print("我是普通方法")

t = Teacher()
t.__init__()
t.class_test()
t.static()
t.common()

