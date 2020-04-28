# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 19:11
# @Author  : guoyunfei.0603
# @File    : inherit01.py

"""
继承
"""
# 第一代机器人
class Robot_One():
    def __init__(self,name,year):
        self.name = name
        self.year = year

    def walk(self):
        print("第一代机器人叫："+self.name,"生产于",self.year,'走的很慢啊')

    def fly(self):
        print("飞的很低")

# 第二代机器人
# class Robot_Two(Robot_One): # 继承第一代机器人、
class Robot_Two():
    # 跟父类方法名一样，叫做方法的【重写】
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print("第二代机器人叫：",self.name,"生产于",self.year,'走的很快')

    def fly(self):
        print("飞的很高，时间长")

    # 跟父类方法名不一样，是子类独有的，叫【拓展】
    def paly(self):
        print(self.name,"会玩游戏",self.age)

# r2 = Robot_Two("乐乐",1990)
# r2.walk()
# r2.paly()

class Robot_Three(Robot_Two,Robot_One):
    def dance(self):
        print(self.name+"第三代机器人会跳舞")



r3 = Robot_Three("星星",19)
r3.paly()

# r3.walk()     AttributeError: 'Robot_Three' object has no attribute 'year'

r3.dance()