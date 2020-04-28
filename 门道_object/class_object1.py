# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 19:37
# @Author  : guoyunfei.0603
# @File    : class_object1.py

class Goods:
    def insert(self,gname,gtitle,gage):
        self.gname = gname     # 类变量
        self._gtitle = gtitle  # 受保护的  单下划线,可以被实例调用 但是不推荐
        self.__gagae = gage     # 私有属性    双下划线，不能被实例调用

        print(gname,gtitle,gage)


    def _Course(self, language, math, english):  # _可以调用
        self.insert("郭云飞", "今年", 22)         # self 可以调用其他方法
        print("期末成绩:",language, math, english)


g = Goods()
g._Course(123,99,89)

g.insert("李逍遥","仙剑奇侠传",19)

print(g.gname)
print(g._gtitle)

# print(g.__gage)   AttributeError: 'Goods' object has no attribute '__gage'







# class Grade:
#     def _Course(self,language,math,english):    # 可以调用
#
#         print(language,math,english)
#
# s = Grade()
# s._Course(100,98,77)