# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 15:54
# @Author  : guoyunfei.0603

import unittest
from ddt import ddt,data,unpack

@ddt # 装饰类
class Demo1_Test(unittest.TestCase):
    # 下面的2,3,4,5代表我们传入的参数, 每次传入一个值
    @data(2,3,4,5)
    # 定义一个value用于接受我们传入的参数
    def test_print(self,value):
        print("打印的结果是：",value)
        self.assertEqual(value,2)


# @ddt
# class Demo2_Test(unittest.TestCase):
#     @data([1,2],[3,4],[5,6],['hi',['你好']])
#     @unpack # 脱一层外套，拆分成
#     def test_print2(self,a,b):
#         print("打印",a,b)


if __name__=='__main__':
     unittest.main()
