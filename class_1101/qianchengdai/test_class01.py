# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 15:15
# @Author  : guoyunfei.0603
import unittest
import HTMLTestRunnerNew
from class_1101.qianchengdai import class_01
suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(class_01))

with open('前程贷.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="前程贷项目11期",
                                              description='登录充值模块', tester='guoyunfei.0603')
    runner.run(suite)
