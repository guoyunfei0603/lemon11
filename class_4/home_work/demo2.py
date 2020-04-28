# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 13:18
# @Author  : guoyunfei.0603
# @File    : demo2.py
"""
2. 自动售卖机：只接受1元、5元、10元的纸币或硬币，最多不超过10块钱。
    饮料只有橙汁、椰汁、矿泉水早餐奶、售价分别是3.5 、4、2、4.5
    写一个函数来表示贩卖机的功能：用户投钱和选择饮料，并通过判断后，给用户吐出饮料和找零
"""
drinks = {"1":3.5,"2":4,"3":2,"4":4.5}

# 饮料
drinks_total = 0
while True:
    choose = input("请选择饮料(1表示橙汁，2表示椰汁，3表示矿泉水，4表示早餐奶，q表示退出):")
    if choose in drinks.keys():
        drinks_total+= drinks[choose]
    elif choose == 'q':
        print("退出成功")
        break
    else:
        print("你输入的选项不存在")
#
# 用户投钱
touqian_total = 0

while True:
    touqian = input("请输入你要投币的金额(只接受1元、5元、10元的纸币或硬币,按q退出)：")
    if touqian == '1' or touqian == '5' or touqian_total == '10':
        touqian_total+=int(touqian)
    elif touqian == 'q':
        print("退出投钱")
        break
    else:
        print("投钱金额错误！")

# 结算
if touqian_total > drinks_total:
    print("你选择饮料的金额是：{0}，投钱的金额是{1},应找零：{2}".format(drinks_total,touqian_total,touqian_total-drinks_total))
if touqian_total<drinks_total:
    print("你选择饮料的金额是：{0}，投钱的金额是{1},还差{2}元".format(drinks_total,touqian_total,drinks_total-touqian_total))
