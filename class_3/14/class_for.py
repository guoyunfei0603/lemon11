# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 19:01
# @Author  : guoyunfei.0603
# @File    : class_for.py
t = [3, 4, 6, 9, 1]
# 完成列表内每个数字的相加

# total = 0
# for item in t:
#     total = total + item
# print("最终的结果：{0}".format(total))

# 打印每个元素的值
# a = [1, 4, 7, 10, 333]
# for item in range(len(a)):  # len(a)表示列表a的长度，里面有几个元素
    # item 遍历 0,1,2,3,4  ，item此时是索引
    # print(a[item])  # a[item] 表示列表a根据索引item取值
# for item in range(5):
#     print(a[item])

# 利用for循环和range函数，完成1-100的相加，求和
# sum = 0
# for item in range(1, 101):
#     sum = sum + item
# print(sum)

# 利用嵌套for循环生成
# *
# **
# ***
# ****
# *****
# for item in range(1,6):
#     print("*" * item)  # item 的值1，2，3，4，5每行输出
                       # '*' * 每行输出

for item in range(5,0,-1):
    print("*" * item)

d = {"name":"令狐冲",'age':15,'sex':'男'}
# for item in d:
#     print(item)      # 遍历的是key
#     print(d[item])   # 根据key，遍历的是value    字典[key]

for item in d.values():
    print(item)
for item in d.items():
    print(item)
    # ('name', '令狐冲')
    # ('age', 15)
    # ('sex', '男')
