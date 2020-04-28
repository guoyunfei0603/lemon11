# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 17:43
# @Author  : guoyunfei.0603
# @File    : class_animal.py

class Animal:
    def __init__(self,name):
        self.name = "盘古"

        print("父类的初始化方法"+self.name)

    def run(self):
        print("我会跑~~")

    def swimming(self):
        print("我会游泳哦~")

    def fly(self):
        print("我可以飞~")