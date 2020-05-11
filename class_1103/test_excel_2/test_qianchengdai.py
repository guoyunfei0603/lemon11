# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 10:16
# @Author  : guoyunfei.0603

import HTMLTestRunnerNew

from class_1103.test_excel_2.demo_excel import Demo_Excel
from class_1103.test_excel_2.qianchengdai import Qian_Cheng_Dai
import unittest

suite = unittest.TestSuite()

test_data = Demo_Excel( 'Demo.xlsx','Sheet1').get_data()

for item in test_data:
    suite.addTest(Qian_Cheng_Dai('test_api', item['url'], eval(item['data']), item['method'], item['expected']))


with open('测试报告.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='前程贷登录充值接口自动化报告',
                                     description='登录充值', tester='断点')

    runner.run(suite)