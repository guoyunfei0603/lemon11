# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 23:58
# @Author  : guoyunfei.0603
# @File    : class_02.py

import unittest
import HTMLTestRunnerNew
from class_1027_unittest.class_01 import TestMathMenthod
# A class whose instances are single test cases.
# 这个类的实例们是一个个单独的实例  所以你要加到TestSuite里面，要多创建几个实例
# instances 单数， 实例
# instances 复数，实例们
# 创建实例

suite = unittest.TestSuite() # 存储用例
# 方法一：
# 只执行一条用例
# 缺点：如果上百条用例一条一条的添加，花费时间长
# suite.addTest(TestMathMenthod('test_add_two_zero'))
# suite.addTest(TestMathMenthod('test_add_two_positive'))


# 方法二：TestLoader  找到以test开头的方法，然后添加到suite
loader = unittest.TestLoader() # 创建一个加载器

# 1) 加载类里面的所有测试用例
suite.addTest(loader.loadTestsFromTestCase(TestMathMenthod)) # 找到这个类里面的所有以test开头的用例

# 2)加载模块里面的所有测试用例
# from class_1027_unittest import class_01 # 具体到模块
# suite.addTest(loader.loadTestsFromModule(class_01)) # 从模块里面去加载，class_01写了两个类，加载模块里面的所有测试用例

"""创建类的实例TestMathMenthod() 需要传参数吗？看有没有初始化函数
1) class TestMathMenthod(unittest.TestCase):  --》继承TestCase，再到TestCase里面找有没有初始化函数
2) 找到了：def __init__(self, methodName='runTest'): --》需要传一个methodName ，就是测试类里面的方法名
"""

# 执行
# 1）txt格式
# file = open("text.txt","w+",encoding="UTF-8") # 必须是w+
# file.close() # 关闭资源


# 2）上下文管理器 推荐使用，不用担心忘记关闭文件资源 -.-
# txt
# with open("test1.txt","w+",encoding="UTF-8") as file:
#     runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)  # verbostity =2 报告详细，推荐
#     runner.run(suite)

# html 格式，浏览器打开
with open("test3.html","wb") as file:
   runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                          verbosity=2,
                                          title="python第11期单元测试报告",
                                          description="guoyunfei.0603",
                                          tester = '小飞')

   runner.run(suite)