# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 21:00
# @Author  : guoyunfei.0603
# @File    : home_work.py

# 编写一个直角三角形
#     *
#     **
#     ***
#     ****
#     *****
#
# for i in range(1,6):# 外层控制行数  i=2
#     for j in range(1,i+1):         j=1,2
#         print("*",end=" ")
#     print(" ")

# 编写一个等腰三角形
                    # ：一共有5行
# @@@@ *            @：空格  4，3，2，1，0
# @@@ *  *          *： 1，2，3，4，5
# @@ *  *  *
# @ *  *  *  *
# *  *  *  *  *

# for i in range(1,6):
#     for k in range(1,6-i):
#         print("",end=" ") # end 不换行输出
#     for j in range(1,i+1):
#         print("* ",end=" ")
#     print(" ")

# 打印九九乘法口诀表
# 1*1 =1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{0}*{1}={2}".format(j,i,i*j),end=" ")
#     print("")














