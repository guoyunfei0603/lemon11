# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 23:53
# @Author  : guoyunfei.0603
# @File    : class_def.py

# 把1-100的累加和 写成一个函数
def mysum(m,n,k=1):
    sum = 0
    for a in range(m,n,k):
        sum += a
    print('累加和',sum)
# mysum(1,101)

# def add(a,b=2): # 默认参数
#     return a+b
#
#     print("这是一个函数~")
# print(add(1))

# 动态参数
def function(*args):
    a = ''
    for item in args:
        a+=item
        a+='、'
    print(a)

function("香蕉",'苹果','橘子')

# 关键字参数 **kwargs

def f(**kwargs):
    print(kwargs)
f(name="张三",age=19,sex='男')