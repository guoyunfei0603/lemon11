# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 10:16
# @Author  : guoyunfei.0603
# @File    : demo1.py
"""
读取指定目录下excel表格内的一行数据 或者多行数据
"""
import xlrd  # xlrd只能读
bk = xlrd.open_workbook(r"d:\test\WorkBook.xlsx")  # 注意：d不能大写
sheet_name = bk.sheet_by_name("老带新")
# 读取单行数据
row_values = sheet_name.row_values(2,3)  # rowx, start_colx=0, end_colx=None
# row_values1 = sheet_name.row_values(3,3)
# row_values2 = sheet_name.row_values(4,3)
# row_values3 = sheet_name.row_values(5,3)
# row_values4 = sheet_name.row_values(6,3)
# print(row_values)
# print(row_values1)
# print(row_values2)
# print(row_values3)
# print(row_values4)

# 我们发现，如果要打印多行，变化的是行数，列数不变，可以用for循环迭代遍历
all_row = []
for i in range(2,7):  # 迭代行
    all_row.append(sheet_name.row_values(i,3))
print(all_row)

