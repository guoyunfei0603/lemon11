# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 9:59
# @Author  : guoyunfei.0603
# @File    : test_basic.py

# str 字符串
# str_1 = "This is my home court！"

# 字符串的切片
# print(str_1[0:4])
# print(str_1[:])
# print(str_1[::-1]) # 反序

# %f可指定小数点后的精度  %.xf   x:指定保留的位数
# num = 1.234
# print("the price is %.2f"%num)

# 字母的大小写转换
# print(str_1.upper()) #大写
# print(str_1.lower()) #小写

str_1 = "This is my home court！"

# 替换  将This替换为this
# print(str_1.replace("T","t"))
# print(str_1.replace(" ","#"))

# # 分割
# print(str_1.split("m"))
# print(str_1.split(' '))

# 去除头尾指定字符或者空格
str_2 = "  hello word!"
# print(str_2.strip())
print(str_2.strip("!"))

# 拼接  +
s3 = str_1+str_2
print(s3)
print("我在复习字符串的操作"+str_2)








