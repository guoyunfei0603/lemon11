# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 13:19
# @Author  : guoyunfei.0603
# @File    : demo4.py
"""
4. 定义一个函数，成绩作为参数传入，如果成绩小于60,则输出不及格。
    如果成绩在60到80之间，则输出良好；
    如果成绩高于80分，则输出优秀，
    如果成绩不在0-100之间，则输出成绩输入错误。
"""
class Grade:
    def my_grader(self):
        grade = int(input("请输入你的成绩："))
        if grade < 60:
            print("不及格")
        elif 60 <grade <= 80:
            print("良好")
        elif grade>80:
            print("优秀")
        elif grade >100 or grade < 0 :
            print("成绩输入错误")
        else:
            print("输入有误")

g = Grade()
g.my_grader()