# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 21:39
# @Author  : guoyunfei.0603
# @File    : run_login.py

import unittest
from class_1027_unittest.home_work import login_recharge

suite = unittest.TestSuite() #创建一个用例集

loader = unittest.TestLoader()
loader.loadTestsFromModule(login_recharge)

suite.run(suite)