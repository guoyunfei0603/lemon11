# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 18:13
# @Author  : guoyunfei.0603

#usr/bin/python
#encoding:utf-8
import unittest
from ddt import ddt,data,unpack

test_data = ([1,2,3],[66,77,88])

@ddt
class TestMath(unittest.TestCase):
    @data(test_data)
    @unpack
    def test_print_data(self,item):
        print('item:',item)




if __name__ == '__main__':
    unittest.main()

