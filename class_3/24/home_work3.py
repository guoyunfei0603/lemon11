# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 16:47
# @Author  : guoyunfei.0603
# @File    : home_work3.py

# 冒泡算法：利用for循环，完成 a = [1,3,9,30,99]的冒泡排序，从小到大
# 核心：两个相邻的元素，依次比较
# 一般最多比较n-1次就可以了  n:元素的个数
a = [3,23,4,100,11]
# [3, 4, 23, 11, 100]
# [3, 4, 11, 23, 100]
# [3, 4, 11, 23, 100]


c= 0
for i in range(1,5):
    for j in range(0,4):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            c +=1
            print('第{0}次:{1}'.format(c,a))
    # print(a)
# print("最终的排序",a)