# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 14:54
# @Author  : guoyunfei.0603
# @File    : hom_work1.py
# 1. 冒泡排序 两个相邻的元素依次比较
#
# def maopao(t):
#     for i in range(len(t)):
#         for j in range(0,len(t)-1):
#             if t[j]>t[j+1]:
#                 t[j],t[j+1]= t[j+1],t[j]
#
#     print(t)
#
# t = [5532,72,521,99,10]
# maopao(t)

"""
2. 自动售卖机:只接受1元、5元、10元的纸币或硬币
可以1元、5元、10元，最多不超过10块钱
饮料有：   可乐，椰汁，矿泉水，早餐奶
售价分别是  3.5，  4，   2，  4.5
写一个函数用来表示贩卖机的功能：
用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零
1. 选择饮料： 字典
2. 投钱：1 5 10 判断金额的面值
3. 判断：钱不够， 钱多了， 钱刚好的情况
"""
# 用户选择饮料
drinks = {"1":3.5,"2":4,"3":2,"4":4.5}
# 存储我们投的钱
total = 0
while True:
    choose = input("请输入你要购买的饮料（1:可乐,2:椰汁,3:矿泉水,4:早餐奶,输入q结束）:")
    if choose in drinks.keys():
        total += drinks[choose]
    elif choose == 'q':
        print("结束选择饮料") # 方便观察
        break
    else:
        print("你输入的选项不存在")

# 用户投币
toubi = 0

while True:
    money = input("请投币:(只能支付1 5 10元面值的纸币或硬币,按q退出)")
    if money == '1' or money =='5' or money == '10':
        toubi += int(money)
        if toubi > total:
            print("你购买饮料的金额是{0}元,投币{1}元,应找零{2}元".format(toubi,total,toubi-total))
        elif toubi < total:
            print("你购买饮料的金额是{0}元,投币{1}元,应再支付{2}元".format(toubi, total, total - toubi))
        elif toubi == total:
            print("你购买饮料的金额是{0}元,投币{1}元,支付完毕！".format(total,toubi))
    elif money == 'q':
        print("退出投币")
        break
    else:
        print("金额不符合")






