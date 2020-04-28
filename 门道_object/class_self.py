# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 9:56
# @Author  : guoyunfei.0603
# @File    : class_self.py
"""
1. 有初始化函数，在创建对象/实例的时候必须给参数
2. 类变量重点理解， 如果不设置，其他方法不能调用属性。

"""
class Animal_Two:
    # 初始化函数，可以把一些公共的属性放到这里面
    # t1 = Animal_Two(150,300) 创建对象，必须传入参数   重点！
    def __init__(self,heigt,weigt):
        self.heigt = heigt  # 把传入的heigt 赋值给self.heigt ，也叫类变量(当前类全局都可以使用)
        self.weigt = weigt
        heigt = "166"
        weigt = "355"

    def tiger(self):

        # print("我是一只东北虎,身高是"+heigt+"体重是"+weigt)   ！！ 不能在其他方法直接调用属性heigt weigt
        # 如果你想调用的话，一定要 self.heigt    self.weigt  这样做，相当于全局变量

        print("我是一只东北虎，身高{0}，体重{1}".format(self.heigt,self.weigt))

    def pig(self,name):
        return "这只猪的名字叫{0}，身高{1}，体重{2}".format(name,self.heigt, self.weigt)

t1 = Animal_Two(150,300) # 第一个实例
t2 = Animal_Two(160,330) # 第二个实例
t3  = Animal_Two(140,350) # 第三个实例

t1.tiger()
t2.tiger()
t3.tiger()

print(t1.pig("丁丁"))


