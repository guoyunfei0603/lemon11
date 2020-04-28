# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 22:27
# @Author  : guoyunfei.0603
# @File    : home_work.py

"""
一个足球队再寻找10-12岁的小女孩，编写一个程序，询问用户的性别（m男，f女）
然后显示一条消息这个人能否加入球队，询问10次后，输出满足条件的人数
"""
# def football(x,y):
#     count = 0
#     for item in range(x,y):
#         sex = input("请问你的性别是：")
#
#         if sex == 'f':
#             age = int(input('请输入你的年龄：'))
#             if 10<= age <=12:
#                 print('希望你加入球队~')
#                 count+=1
#             else:
#                 print("年龄不符合标准")
#         else:
#             print('不符合哟~')
#     print("满足条件的人数：{0}".format(count))
# football(1,5)
"""
输入num为四位数，对其按照如下的规则进行加密
1. 每一位分别加5，然后分别将其替换为该数除以10取余后的结果
2. 将该数的第1位和第四位互换，第二位和第三位互换
3. 最后合起来作为加密后的整数输出
"""
# def num():
#      num = input('请输入一个四位数：')
#      num1 = ''
#      for item in num:
#           # print(item)
#          # num_2 = num_1%10
#           num1+= str((int(item)+5)%10)
#           last_num = num1[::-1]
#      print(last_num)
# num()

"""
生成一个随机整数，1-9，
# """
# import random
# try:
#      num = random.randint(1,10)
#      user = int(input("请输入1-9的数字"))
#      print('电脑输入的是{0}'.format(num))
#      if num == user:
#           print('相等')
#      elif num > user:
#           print('你输了')
#      elif num < user:
#           print('你赢了')
#      else:
#           print('重新输入')
# except:
#      print('输入有误')
"""
写一个函数，传入一个列表，如果长度大于2，仅保留前2位
"""
def two(x):
     # x = [2,3,4,5]
     if len(x)>2:
          return  x[:2]
x = [1,2,3]
print(two(x))




