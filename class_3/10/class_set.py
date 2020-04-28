# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 14:48
# @Author  : guoyunfei.0603
# @File    : class_set.py
#集合（set）是一个无序的不重复元素序列。
# parame = {value01,value02,...}


# 空集合
# s = set()
# print(s)

t = [1,2,2,1,3]
s1 = set(t)
# print(s1)         <class 'set'>
# print(type(s1))

s2 = {"a","a","b","c"}  # 去重
print(s2)