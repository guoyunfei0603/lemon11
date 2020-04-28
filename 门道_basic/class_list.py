# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 22:26
# @Author  : guoyunfei.0603
# @File    : class_list.py

t = [1,3,4,5,6,"测试"]

# 支持切片
# print(t[-3])
#
# print(len(t))

# 遍历
# for item in range(len(t)):
#     print(t[item])

# 增
t.append("一次只能追加一个")
print(t)

t.append(("追加一个元组,列表",'???',"test"))   # 都可以
print(t)

print(t.index("测试"))  # 返回列表值的索引

t1 = ["测试","工程师","666"]
# 删
t1.pop(0) # 根据索引下标删除
print(t1)

# 改
t1[0] = "我是大佬"
print(t1)

# 查  切片，

# 列表解析
# 一行代码 包含for循环 if语句   快速生成一个列表
# 格式：[x for循环 if判断]     可以有多个x 多个for循环 多个if

# 快速生成1个1-10的列表
print([(i) for i in range(1,11) ])

print([(x,y) for x in range(1,5) for y in range(1,10) if x>2 if y==5])

str1 = 'NKSZ94T2004080058'
print(len(str1))