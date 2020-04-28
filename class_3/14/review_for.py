# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 14:56
# @Author  : guoyunfei.0603
# @File    : review_for.py

# 使用内置 enumerate 函数进行遍历:
# s = ["秦","时","明",'月']
# for j,item in enumerate(s):
#     print(j,item)

# for 循环 1-100 所有整数的和
# my_sum = 0
# for item in range(101):
#     my_sum+=item
# print("1-10所有整数的和:",my_sum)

# for 循环 1-100 所有奇数的和
# count = 0
# for item in range(1,101):
#     if item %2 !=0:
#         count+=item
# print("1-100的奇数和是:",count)

# 使用循环嵌套来实现99乘法法则:
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{0}*{1}={2} ".format(i,j,i*j),end=" ")
#     print("")

# 直角三角形
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# 冒泡排序 ：两个相邻的元素比较
t = [14,90,3,44,10,5]
for i in range(1,6):
    for j in range(0,5):
        if t[j]>t[j+1]:
            t[j],t[j+1]=t[j+1],t[j]
    print(t)

