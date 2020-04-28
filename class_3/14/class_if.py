# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 17:41
# @Author  : guoyunfei.0603
# @File    : class_if.py

# 条件语句 判断 if
# 支持 逻辑/成员/比较运算符

'''
一家商城在促销，如果购买金额在50~100元（包含50和100）之间 会给10%的折扣
如果购买金额大于100元，会给20%的折扣，。
编写一个程序，询问其价格，显示出折扣（10%或20%）和最终价格
'''
price = int(input("请输入购买的价格："))
# price.isdigit()
if 100 >= price >= 50:
    print("10%的折扣~")
    final_price = price * 0.9
    print('最终价格：',final_price)
elif price > 100:
    print("20%的折扣~")
    final_price = price * 0.8
    print("最终的价格为：", final_price)
elif 50 > price >=0:
    print("不好意思，没有折扣，最终价格为：",price)
else:
    print("请重新输入，谢谢~~")

