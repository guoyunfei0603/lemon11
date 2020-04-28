# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 13:17
# @Author  : guoyunfei.0603
# @File    : demo1.py

"""
1. 写一个函数，可以完成任意指定整数的相加，并返回结果:

"""


class Work:
    # 注意：当把函数变成类的时候，一定要加self！
    def add_num(self,*args):
        my_sum = 0  # 求和,最开始的值是0
        # 遍历出每个传入的值
        for i in range(len(args)):
            my_sum += args[i]
        return my_sum

    # print_add = add_num(9,8,4,3,2,221,88)
    # print(print_add)
w = Work()

c = w.add_num(1,10,22)
print(c)
