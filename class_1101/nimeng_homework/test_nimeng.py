# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 21:08
# @Author  : gyf

from class_1101.nimeng_homework import nimeng
import unittest
import HTMLTestRunnerNew

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(nimeng))

with open('nimeng01.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="结合Excel读取数据完成接口自动化",
                                     description="测试", tester="gyf.0603")
    runner.run(suite)
