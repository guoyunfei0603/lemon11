# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 17:08
# @Author  : guoyunfei.0603
# @File    : class_cls.py

# 类 首字母大写
# 类里面有属性和方法
# self 是实例本身，类本身，可以调用类里面的属性和方法

class Teacher:
    name = '秦朗'
    age = 18
    interest = "游泳"
    work = "老师"

    def name_1(self):
        print("华华老师~")

    def name_2(self):
        print("莎莎老师~")

    def dance(self,name):
        self.name = name

        print("{0}会跳舞哦!喜欢{1}".format(self.name,self.interest))

    def person(self):
        print(self.name,self.age,self.interest,self.work)


# 调用类里面的方法，跟普通方法的使用是一样的
# 创建对象  对象名.函数名 调用
t1 = Teacher()
t1.name_1()
t1.name_2()
t1.dance("华华")
t1.person()
Teacher().dance("莎莎") # 也可以类名.函数名调用