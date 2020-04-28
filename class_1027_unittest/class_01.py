# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 23:31
# @Author  : guoyunfei.0603
# @File    : class_01.py

# 接口测试的本质就是测试类里面的函数，通过数据驱动
# 单元测试的本质：测试函数 代码级别  通过代码级别测试
# 单元测试的框架：unittest+接口  pytest+WEB--》接口
# 高级玩法：pytest+jenkins+allure    前提是：学会unittest

# 功能测试：
# 1. 写用例    TestCase
# 2. 执行用例   1)TestSuite:存储用例   2：TestLoader：找用例，加载用例，存到1的TestSuite
# 3. 对比实际结果和期望结果    断言 assert
# 4. 出具测试报告 TextTestRunner

import unittest

# 写一个测试类，对我们写的math_method模块里面的类 进行单元测试
from class_1027_unittest.math_method import MathMenthod # 测试的目标类

class TestMathMenthod(unittest.TestCase):
    # 编写测试用例
    # 一个用例就是一个函数 不能传参，只有self关键字
    # 所有的用例都是test开头  建议test_

    def setUp(self):
        print("我要开始执行测试用例了-----")

    def tearDown(self):
        print("我已经执行完毕用例了#######")

    """
    1. setUp和terarDown 可以不写嘛？ 爱写不写，必要的时候再写
    2. 什么时候执行setUp？    执行每一条用例之前
       什么时候执行tearDown？ 执行完每一条用例后
    3. 就像一个夹心饼干，把每一个用例包起来
    4. 如果你有操作必须在执行用例之前准备好，那就放到setUp里面，
       如果你有操作必须在执行完成后清除掉，那就放到tearDown里面，  比如：操作数据库，连接--关闭(后期会用到)
    """

    def test_add_two_positive(self):# 测试两个正数相加
        res = MathMenthod(1,1).add()
        print("1+1的结果是：",res)
        try:
            self.assertEqual(3,res,'**两个正数相加出错了**') # 断言里面，msg是用例执行失败才会提示
        except Exception as e:
            print("出错了！断言错误是{0}".format(e))
            raise e # 异常处理完了要抛出去

        """def assertEqual(self, first, second, msg=None):
        first: 预期结果
        second: 实际结果
        msg:可选参数，如果报错提示什么
        
        断言需要掌握：
        1. assertEqual(a,b)      判断a == b
        2. assertNotEqual(a,b)   判断a != b
        3. assertIsNone(x)       判断x 是None
        4. assertIsNotNone(x)    判断x 不是None
        5. assertIn(a,b)         判断a in b
        6. assertNotIn(a,b)         判断a not in b
        
        """

    def test_add_two_zero(self):# 测试两个0相加
        res = MathMenthod(0,0).add()
        print("0+0的结果是：",res)
        self.assertEqual(0, res)

    def test_add_two_negative(self):# 测试两个负数相加
        res = MathMenthod(-1, -2).add()
        print("-1+-2的结果是：", res)
        self.assertEqual(-3, res)

class TestMul(unittest.TestCase):

    def test_mul_two_positive(self):
        res = MathMenthod(5,10).mul()
        print("5乘以10的结果是",res)
        self.assertEqual(50, res)

    def test_mul_two_zero(self):
        res = MathMenthod(0,0).mul()
        print("两个0相乘的结果是",res)
        self.assertEqual(0, res)


# if __name__ == '__main__':
#     unittest.main() # 执行所有的用例

# 如果你不在当前模块执行所有测试用例，就用到了suite --》class_02.py
"""
... 执行成功
E   代码错误，检查你写的代码
F   用例不通过

# 鼠标光标在函数那个位置就可以执行那一个函数，
  在所有函数下可以执行全部函数

# 执行顺序是按照ASCII编码 --》 abcdefghijklm"n"o"p"qrstuvwxy"z"
结果：
-1+-2的结果是： -3
1+1的结果是： 2
0+0的结果是： 0

positive
zero
negative
"""

