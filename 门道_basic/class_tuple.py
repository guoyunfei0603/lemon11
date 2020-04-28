# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 16:43
# @Author  : guoyunfei.0603
# @File    : class_tuple.py

# 元组
# t1=(3,5,10,9,100,50)
# 取值  正  反
# print(t1[2])
# print(t1[-3])

# 切片【重要！】
# print(t1[1:4])

# 一维
t2 = ("江金莲","女",28,"高级软件测试工程师")

# for item in range(len(t2)):
#     print(t2[item])

# 遍历 【非常重要！】
# for iem in t2:
#     print(iem)

# 优化版本
# for item in range(len(t2)):  # len() 函数返回元素的个数
#     # print(item) # 遍历的是索引值
#     print(t2[item])

# 二维 ：就是圆括号里面又套了一层
# 多维 ：嵌套多层
t3=(
    ("江金莲","女",28,"高级软件测试工程师"),
    ("王旭婷","女",22,"中级软件测试工程师"),
    ("郭云飞","男",22,"中级软件测试工程师")
    )
# 我想取到数字年龄
# print(t3[0][2])
# print(t3[1][2])
print(t3[2][2])



# # 推荐这种写法
# for i in range(len(t3)):
#     for j in range(len(t3[i])):
#
#         print(t3[i][j])

t3=(
    ("江金莲","女",28,"高级软件测试工程师"
    ("聪明",

    )),
    ("王旭婷","女",22,"中级软件测试工程师"),
    ("郭云飞","男",22,"中级软件测试工程师")
    )

for i in range(len(t3)):
    for j in range(len(t3[i])):
        print(i,j,t3[i][j])
