# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 15:59
# @Author  : guoyunfei.0603
# @File    : review_if.py

# 1-100的偶数和
# i = 1
# count = 0
# while i<=100:
#     if i %2 == 0:
#         count+=i
#     i+=1            # i自增
# print("1-100的偶数和是：{0}".format(count))

s = ["阿里巴巴","腾讯","百度","字节跳动"]

for item in s:
    if item == '百度':
        continue
    print(item)

