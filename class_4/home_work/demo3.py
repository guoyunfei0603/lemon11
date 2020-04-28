# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 13:18
# @Author  : guoyunfei.0603
# @File    : demo3.py
#
"""
3. 写函数，将姓名、性别、城市作为参数，并且性别默认为f(女)，
    如果城市在长沙并且性别为女，则输出姓名、性别、城市，并返回True，否则返回False

"""


# def message(name,sex,city):
class My_Msg:
    def message(self):
        while True:
            name = input("请输入你的名字：")
            sex = input("请输入你的性别（f:女，M：男）：")
            city = input("请输入你的城市：")
            # print("###################")
            close = input("输入q结束：")
            if close == 'q':
                break
            else:
                if city == '长沙' and sex == 'f':

                    return "你的名字是{0},性别是女,城市是{1}".format(name, city)
                else:
                    return False


# m = message()
#
# print(m)

my = My_Msg()

m = my.message()
print(m)