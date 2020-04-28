# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 23:35
# @Author  : guoyunfei.0603
# @File    : class_file.py

# 文件操作
"""
w:写     write
r:读     read
a:追加   append
"""
# f = open("test_01.txt",'w',encoding='utf-8')
# f.write("我可真是笨呢")

# f1 = open('test_01.txt','r',encoding='utf-8')
#
# print(f1.read())

f2 = open('test_01.txt','a',encoding='utf-8')
f2.write('\n 不好意思啦')
