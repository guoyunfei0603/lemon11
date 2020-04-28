# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 19:03
# @Author  : gyf

import HTMLTestRunnerNew
import unittest
from class_1101.home_work import class_ke

suite = unittest.TestSuite() # 创建一个用例存储容器

loader = unittest.TestLoader()  # 加载用例到suite

suite.addTest(loader.loadTestsFromModule(class_ke))

# z=执行
with open("test.html","wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="柠檬班第11期练习作业",
                                     description="课堂派登录接口自动化测试", tester="gyf.0603")

    runner.run(suite)