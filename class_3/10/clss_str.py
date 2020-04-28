# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 10:24
# @Author  : guoyunfei.0603
# @File    : clss_str.py

# 字符串的常见操作
s = 'hello！'
print(s)

# 字符串切片 从0开始算起，
# s[x:y:z]  x:索引起始点   y:索引结束点  z:步长，默认为1   （取头不取尾）
#  h   e   l   l   o   !
#  0   1   2   3   4   5    正序
# -6  -5  -4  -3  -2  -1    反序

# 拿到！
print(s[5])
print(s[-1])

# 拿到所有
print(s[::1])
print(s[0:])
s = "python!"
#
print(s[::2])

# 排序为!olleh
print(s[-1:-8:-1]) #-1,-2,-3,-4,-5

# len(数据) 获取长度，有多少个元素
print(len(s))

s1 = 'teacher'
# 字符串的切割 split()
print(s1.split('t'))
print(s1.split('e',2)) # 可以指定切割的次数

# 字符串的替换，字符串.replace()
print(s1.replace('e','E',1)) # 可以指定替换的次数

# 字符串过滤指定头尾的字符 ，字符串.strip()
s2 = '112 teache r 1'
print(s2.strip())    # 如果没有指定，则去掉头尾的空格
print(s2.strip('1')) # 可以删除指定头尾的字符，中间的不可以
# 字符串的拼接 用+，
print(s1+s2)

# ,连接不是拼接，只是输出每个元素
print(s1,s2)
