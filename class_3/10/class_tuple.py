# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 15:25
# @Author  : guoyunfei.0603
# @File    : class_tuple.py
# 元组
# a = ()
a = (1)
# print(type(a))    <class 'int'>
b = (2,) # 只有一个元素的时候，要加逗号
# print(type(b))    <class 'tuple'>

# 切片
t = (10,20,"teahcer",(999,100),[66,77,88])
# print(t[1])
# print(t[:2])
# print(t[::2])

# 元组不能增删改，但也不是必须
# t[1] = 111
# print(t)TypeError: 'tuple' object does not support item assignment

# 元组如果包含列表，可以修改列表内的元素
# t[-1][0] = 'name'
# print(t)

# 列表内如果包含元组，不能修改元组内部元素， 可以把整个元组修改
a = [1,2,3,(555,666)]
# a[-1][0] = 8
# print(a)  TypeError: 'tuple' object does not support item assignment
a[-1] = "整个元组修改"
# print(a)  [1, 2, 3, '整个元组修改']
