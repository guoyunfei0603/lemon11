# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 20:17
# @Author  : guoyunfei.0603

from ddt import ddt,data,unpack
import unittest
"""
（1）* test_data 脱一层外套
（2）unpack 根据 逗号，  再脱一层外套  
（3）最多只能 脱2层外套
（4）要放到代码最后面执行，不然会报错
"""


'''
test_data = [[1,2,6],[3,4,9]]
@ddt
class Test_Data(unittest.TestCase):
    @data(*test_data)
    @unpack
    def test_02(self,a,b,c):
        print(a[1])
        print(b)
        print(c)

    # def test_03(self,a):
    #     print(a[0])
    
 # (5) 如果你要对字典进行unpack  key要与你字典的key对应
   (6) 参数5个以内可以使用unpack 
'''
test_data = [{'no':101,'name':'断点','age':'18'},
             {'no':102,'name':'水迹','age':'19'}]

@ddt
class Test_Data(unittest.TestCase):

    @data(*test_data)
    @unpack
    def test(self,no,name,age):
        print(no)
        print(name)
        print(age)




