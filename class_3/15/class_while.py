# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 11:00
# @Author  : guoyunfei.0603
# @File    : class_while.py
#
# name = ['张三','里斯','王五','召开','顺子']
#
# a = input("请输入一个名字：")
# if a in name:
#     print('这个人在班级里面')
# else:
#     print('这个人不在~')

# whlie 循环 1-100整数相加
a = 1
sum = 0
while a <= 100:
    sum = sum + a
    a = a + 1

# print('1到100的整数和是{0}'.format(sum))
'''
设置一个登录程序，不同用户名和对应命名存在一个字典里，输入正确的用户名和密码登录
首先输入用户名，如果用户名不存在或者为空，则一直提示：输入正确的用户名
当用户名输入正确，提示去输入密码，如果密码和用户名不正确，则提示密码错误请重新输入
如果密码输入错误三次，提示还有几次机会
当用户名和密码都输入成功，提示：登录成功
# '''
# username_pwd = {'zhangsan':'123456','lisi':'123','abc':'666'}
# count = 3 # 记录密码输入次数
#
# while True:
#     user_name = input('请输入用户名：')
#     if user_name in username_pwd.keys():
#         while count>0:
#             pwd = input('请输入密码：')
#             if pwd == username_pwd[user_name]:
#                 print('密码正确，登录成功')
#                 break
#             else:
#
#                 count =count -1
#                 print('密码错误，请重新输入~,还剩下{0}次机会'.format(count))
#         break
#     elif user_name not in username_pwd or user_name == '':
#             print('请输入正确的用户名~')

# 实现一个九九乘法口诀表 1 * 2 = 2
# for j in range(1,10):
#     for k in range(1,j+1):
#
#         print(" {0} * {1} = {2} ".format(j,k,j*k),end=' ')
#     print(" ")
# #

# 1 * 1 = 1
# 2 * 1 = 2   2 * 2 = 4
# 3 * 1 = 3   3 * 2 = 6   3 * 3 = 9

# i = 1
#
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(" {0} * {1} = {2} ".format(j, i, i * j), end=' ')
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d*%d=%d" % (j, i, (j * i)), end="\t")
#         j += 1
#     print()
#     i += 1

# import class_3.test

from class_3.test import num
num()

