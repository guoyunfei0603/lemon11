# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 15:49
# @Author  : guoyunfei.0603
# @File    : class_dict.py

# 字典 dict     key:value形式
# key必须是唯一的
a = {"name":"郭云飞",
     "age":22,
     "gender":"男",
     "money":[100,200,300]}
# print(a)

# value 可以存放任意类型
# 新增
a["interest"] = "sing"
# print(a)

# 修改
a["name"] = "gyf"
print(a)