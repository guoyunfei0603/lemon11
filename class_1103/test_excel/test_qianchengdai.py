# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 10:16
# @Author  : guoyunfei.0603

import HTMLTestRunnerNew
from class_1103.test_excel.qianchengdai import Qian_Cheng_Dai
import unittest

test_data = [{'url':'http://test.lemonban.com/futureloan/mvc/api/member/login',
              'data':{"mobilephone": "18535653506", "pwd": "python123"},'expected':'登录成功','method':'post'},
             {'url':'http://test.lemonban.com/futureloan/mvc/api/member/login',
              'data':{"mobilephone": "18535653506", "pwd": ""},'expected':'密码不能为空','method':'post'},
             {'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
              'data':{"mobilephone": "18535653506", "amount": "10000"},'expected':'充值成功','method':'post'},
             {'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
              'data':{"mobilephone": "18535653506", "amount": "-10"},'expected':'请输入范围在0到50万之间的正数金额','method':'post'}]

suite = unittest.TestSuite()
for item in test_data:

    suite.addTest(Qian_Cheng_Dai('test_api', item['url'], item['data'], item['method'], item['expected']))
    # print( item['url'], item['data'], item['method'], item['expected'])

with open('前程贷.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='前程贷登录充值接口自动化报告',
                                     description='登录充值', tester='断点')

    runner.run(suite)