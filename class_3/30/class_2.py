# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 18:17
# @Author  : guoyunfei.0603
# @File    : class2.py
class TeacherTwo():
    interest = "运动健身"
    work = "地理老师"
    play_game = "植物大战僵尸"

    @classmethod  # 类方法
    def swmming(cls):
        print("我会游泳")


    def dance(self,name): # 实例方法
        print("{0}喜欢{1}和{2}".format(name,self.interest,self.play_game))
        self.swmming()
        self.drive()
    @staticmethod
    def drive():
        print("我会开小汽车")


t1 = TeacherTwo()
t1.drive()
t1.swmming()
t1.dance("小花")
TeacherTwo().drive()
"""
1. 实例方法self 类方法cls 静态方法（普通方法） 实例和类名都可以直接调用
2. 不同点：静态方法 和 类方法 不可用调用类里面的属性值，如果你要参数 请自己传递参数
3. 什么时候去定义为静态和类方法  当你的某个函数和其他的类函数，类属性没有关系的时候
    因为,静态函数和类方法不能调用类里面的属性值 
"""
