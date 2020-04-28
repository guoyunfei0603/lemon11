# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 10:04
# @Author  : guoyunfei.0603
# @File    : class_def.py

# 函数
# def 函数名()     小写，驼峰式  见名知意

# 无参无返回
# def f_sum():
# #     total = 0
# #     for item in range(1,101,1):
# #         total += item
# #     print(total)
# #
# # f_sum()

# 有参无返回
# def f_sum(start,end,step):
#     total = 0
#     for item in range(start,end,step):
#         total += item
#     print(total)
#
# f_sum(2,50,1)

# 有参有返回
# def f_sum(start,end,step):
#     total = 0
#     for item in range(start,end,step):
#         total += item
#     return total
#
# result = f_sum(1,101,1) # 当有return 返回给调用者，需要一个变量来接收
# print(result)      # 可以打印到控制台

# return返回值  你想怎么玩就怎么玩
# print(result+100)
# if result >100:
#     print("真棒")

def f_test(name,sex,age=10,work=True):
    """

    :param name:
    :param sex:
    :param age:
    :param work:
    :return:
    """
    print(name,sex,age,work)

f_test("郭云飞","男") # 有默认参数可以不用写
f_test("郭云飞","男",20)
f_test("郭云飞","男",25,False)
f_test("男","郭云飞",30)  # 位置参数是一一对应的，按照顺序一个一个填写
f_test(name="张小盒",age="22",sex="男")  # 指定参数，可以不按顺序来