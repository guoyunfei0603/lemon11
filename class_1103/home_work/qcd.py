# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 15:11
# @Author  : guoyunfei.0603

from API_AUTO.tools.new_http import HttpRequest
from API_AUTO.tools.test_fanshe import GetData
import unittest
import json


class Qian_Cheng_Dai(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def __init__(self,methodName,method,url,data,headers,expected):
        super(Qian_Cheng_Dai,self).__init__(methodName)
        self.method = method
        self.url = url
        self.data = data
        self.headers = headers
        self.expected = expected

    def test_api(self): # 接口用例
        ''' 这里有问题，想不通为什么要写个初始化函数传参'''
        res = HttpRequest().http_request(self.method,self.url,json.dumps(self.data),
                                         self.headers,getattr(GetData,'Cookie')) # getattr获取‘Cookie’属性
        # 如果有cookie，就存到‘Cookie’这个属性里面
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)
        try:
            self.assertEqual(self.expected,res.json()['code'])
        except AssertionError as e:
            raise e
        return res


if __name__ == '__main__':
    unittest.main()