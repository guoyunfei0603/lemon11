# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 15:17
# @Author  : guoyunfei.0603
# @File    : class_list.py

# 空列表
# a = []

# 任意类型
# a = [1, 2, 3, 'hello', (5, 6, 7)]
# print(len(a))
# print(a[2:4])
# print(a.index('hello'))  返回索引

# print(a[3][-2])
# append 末尾追加
# a.append('test')

# insert 插入
# a.insert(3,'第三个')

# pop 删除
a = [1, 2, 3, 'hello', (5, 6, 7)]
# a.pop(4) # 指定的索引

print(a)

# 修改
a[0] = 0
print(a)