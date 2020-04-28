# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 17:36
# @Author  : guoyunfei.0603
# @File    : review_def.py

def add(a,b): #形参/位置参数
   return a+b

# print(add(1,10))

# def sub(a,b=3): #默认参数，必须放到位置参数后面
#     print(a-b)
# sub(10)

try:
    def method(*args): # 不定长函数，可以添加任意个参数
        print("我喜欢玩{0}、{1}、{2}".format('王者荣耀','穿越火线'))
    method()
except Exception as e:
    print("**错误日志**",e)

