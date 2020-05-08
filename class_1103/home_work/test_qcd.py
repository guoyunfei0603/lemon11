# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 15:15
# @Author  : guoyunfei.0603
import unittest
import HTMLTestRunnerNew
from class_1103.home_work.qcd import Qian_Cheng_Dai
from API_AUTO.tools.do_excel import Do_excel
from ddt import ddt,data

test_data = Do_excel('lemon.xlsx','test').get_data()

# test_data = [{'method':'post','url':'http://120.78.128.25:8766/futureloan/member/login','data':{"mobile_phone": "18535653506"},'headers':{'X-Lemonban-Media-Type':'lemonban.v2','Content-Type': 'application/json'},"pwd": "python123",'expected':0},
#              {'method':'post','url':'http://120.78.128.25:8766/futureloan/member/login','data':{"mobile_phone": "","pwd": "python123"},'headers':{'X-Lemonban-Media-Type':'lemonban.v2','Content-Type': 'application/json'},'expected':2},
#              {'method':'post','url':'http://120.78.128.25:8766/futureloan/member/login','data':{"mobile_phone": "185","pwd": "python123"},'headers':{'X-Lemonban-Media-Type':'lemonban.v2','Content-Type': 'application/json'},'expected':2}]

suite = unittest.TestSuite()

# 示例的方式去加载用例 --method，url，data，headers，expected
for item in test_data:

    suite.addTest(Qian_Cheng_Dai("test_api",item['method'],item['url'],item['data'],item['headers'],item['expected'] ))

with open('前程贷.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="前程贷项目11期",
                                              description='登录模块', tester='guoyunfei.0603')
    runner.run(suite)
