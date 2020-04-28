# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 18:23
# @Author  : guoyunfei.0603
# @File    : home_work.py
"""
生成一个随机整数，从1—9取出来，然后输入一个数字，
如果大于，就打印bigger,如果小于就打印less，等于就打印equal
"""
# import random
#
# r = random.randint(1, 9)
# num = int(input('请输入一个数字：'))
#
# if num > r:
#     print('随机数是：', r, 'bigger')
# if num < r:
#     print('随机数是：', r, 'less')
# if num == r:
#     print('随机数是：', r, "equal")

"""
一个足球队，寻找10—12岁的女孩子踢球，询问10次后输出结果
男孩m，女孩f表示  
询问年龄及性别,输出满足条件的人数
"""
# sum = 0
# for item in range(1,5):
#     age = int(input('请问你的年龄是：'))
#     sex = input('请问你的性别是：')
#
#     if 12>= age >=10 and sex == 'f':
#
#         print('你符合我们球队的标注，希望你加入~')
#         sum = sum + 1
#     else:
#         print('不好意思，不符合~')
# print('满足条件的人数{0}'.format(sum))

for i in range(1,6,2):  # 1,3,5
    print(i)

print(list(range(1,10,2))) # 方便观察而已