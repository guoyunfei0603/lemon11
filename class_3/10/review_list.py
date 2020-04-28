# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 10:49
# @Author  : guoyunfei.0603
# @File    : review_list.py

# 列表
t1 = [5, 15, 10, 20, 100]
#
# # 切片
# print(t1[:])
# print(t1[0:5:2])
print(max(t1))  # 返回列表的最大值

# append 在列表的末尾追加
t1.append("江小白")  # 一次只能添加一个元素
# print(t1)

# extend 追加另一个列表
# t2 = [1,2,3,4,5]
# t1.extend(t2)
# print(t1)

# count 统计某个元素在列表出现的次数
t3 = ["hello", "hi"]
# print(t3.count("hi"))

# insert 插入指定对象
t3.insert(1,"name")
# print(t3)
# index
# print(t3.index("hi"))

# pop 根据索引删除
print(t3.pop(-1))
print(t3)


# 从小到大
t4 = [3,44,23,100,88]
# print(sorted(t4))
#

# 有问题，，
# teacher= " "
# for item in range(1,11):
#     teacher+=item
#     print("第{0}个老师".format(teacher))
