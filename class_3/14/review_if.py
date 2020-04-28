# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 16:41
# @Author  : guoyunfei.0603
# @File    : review_if.py

# 输入一个数字，判断能否整除2和3

# num = int(input("请输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print("该数能整除2和3")
#     else:
#         print("能整除2但不能整除3")
# else:
#     if num%3==0:
#         print("能整除3但不能整除2")
#     else:
#         print("你输入的数字不能整除 2 和 3")

# while True:
#     s =input("请输入你反馈的问题： 1:小程序相关  2:移动收银相关 3:云店通相关 4:其他问题 5:输入#结束:")
#     if s == '1':
#         print("这里是小程序相关的问题")
#     elif s == '2':
#         print("这里是移动收银相关的问题")
#     elif s=='3':
#         print("这里是云电通相关的问题")
#     elif s =='4':
#         print('请问有其他什么问题？')
#     elif s == '#':
#         print('结束程序~')
#         break

# 输入num为四位数，对其按照如下的规则进行加密
# 1. 每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2. 将该数的第1位和第四位互换，第二位和第三位互换
# 3. 最后合起来作为加密后的整数输出

num=input("请输入一个四位数：")
s = ''
for item in num:
    result = (int(item)+5)%10
    s+=str(result)
    num_result = s[::-1]

print(num_result)