# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 22:18
# @Author  : guoyunfei.0603
# @File    : class_dict.py

d = {"status":-1,
     "data":"null",
     "msg":"data error",
     "person":{"name":"郭云飞",
               "age":22,
               "sex":"男"}
     }

# print(d.items())
# print(d.get("msg"))
print(d.keys())
# print(d.values())

# for key,value in d.items():
#     print(key,value)

# 拿到年龄age ,先获取person 再获取age
# print(d.get("person").get("age"))

# print(d.get("person").get("sex"))

