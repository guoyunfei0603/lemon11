# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 20:00
# @Author  : guoyunfei.0603

from ddt import ddt,data,unpack
import unittest
test_data = [1,2,3]

t_data = [(1,2,3),('a','b','c'),('甲','乙','丙')]

@ddt# 装饰测试类
class Test_Data(unittest.TestCase):
    # 装饰测试方法，拿到几个数据，就执行几条用例

    # @data(test_data)  # 不加 * 号，拿到了1个数据
    # @data(*test_data) # 加了 * 号后，脱了一层外套，拿到了3个数据   -->只能脱一层外套
    @data(*t_data)

    def test_01(self,item):
        print('结果：',item)

