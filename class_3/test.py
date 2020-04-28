# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 23:09
# @Author  : guoyunfei.0603
# @File    : test.py
def num():
    num = input('请输入一个四位数：')
    num1 = ''
    for item in num:
        # print(item)
        # num_2 = num_1%10
        num1 += str((int(item) + 5) % 10)
        last_num = num1[::-1]
    print(last_num)

if __name__ == '__main__':

    num()
