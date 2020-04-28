# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 10:35
# @Author  : guoyunfei.0603
# @File    : class_vararguments.py
# 变参（动态参数）  *args   **kwargs


# 1. *args
def f_sum(*args):  # *args：可以匹配多个参数
    total = 0
    for item in range(args[0], args[1], args[2]):  # strt,end,step
        total += item
    return total


result = f_sum(1, 101, 2)  # 实参，实际传进去的参数


# print(result)

def f_test(*args):
    # print("我是一个软件测试工程师，我会"+str(args))
    # print("我是一个软件测试工程师，我会",args)  # 用,逗号连接会多一个空格

    return args   # 是一个元组


rs = f_test("接口测试", "自动化测试", "性能测试")
# print(type(rs)) # 返回的是一个元组类型<class 'tuple'>

# for item in range(len(rs)):  # len函数，作用是获得元素的个数
#     print(rs[item])


my_list = [2,4,12,3,10]
my_tuple = ("你好","世界","未来")
my_str = "怎么会迷上你"
my_dict = {"name":"鸣人","age":18,"skill":"螺旋丸"}
my_set = {"佐助","轮回眼","须佐能乎","月读","手里剑"}

# print(len(my_list))     #5
# print(len(my_tuple))    #3
# print(len(my_str))      #6
# print(len(my_dict))     #3
# print(len(my_set))      #5

# 用for循环把以上全部都迭代出来

def f_list():
    for i in range(len(my_list)):
        print("my_list:",my_list[i])

    rs = [i for i in my_list]  # 列表解析 ，
    # print(rs)
    # print(rs[1])          # 是一个列表支持切片等操作,不过 原列表就可以直接操作，没必要这么麻烦
    # rs.append("今天")
    # print(rs)

f_list()



# def f_tuple():
#     for i in range(len(my_tuple)):
#         print(my_tuple[i])
#
#     rs = [i for i in my_tuple]
#     print(rs)
# f_tuple()

# def f_str():
#     for i in range(len(my_str)):
#         print(my_str[i])
#     rs = [i for i in my_str]
#     print(rs)
# f_str()

# def f_dict():ict.items():
#         print(key,value)
#     for key,value in my_d

    # rs = [i for i in my_dict.items()]
    # print(rs)

# f_dict()

# def f_set():
#     for i in my_set:
#         print(i)
#     rs = [i for i in my_set]
#     print(type(rs)) # <class 'list'>
# f_set()       # set 是无序不重复的集合
