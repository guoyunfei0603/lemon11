# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:18
# @Author  : guoyunfei.0603

import unittest
import requests
from API_AUTO.tools.http_request import HttpRequest
from API_AUTO.tools.test_fanshe import GetData

class Qian_Cheng_Dai(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self,methodName,url,data,method,expected):
        super(Qian_Cheng_Dai,self).__init__(methodName) # 超继承 保留父类（TestCase）的init函数里面的参数methodName
        self.url = url
        self.data = data
        self.method =method
        self.expected = expected


    def test_api(self):

        res = HttpRequest().http_request(self.url,self.data,self.method,getattr(GetData,'Cookie'))
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)

        try:
            self.assertEqual(self.expected,res.json()['msg'])
        except AssertionError as e:
            raise e