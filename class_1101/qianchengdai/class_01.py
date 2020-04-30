# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 15:11
# @Author  : guoyunfei.0603

from API_AUTO.tools.new_http import HttpRequest
import unittest
import json

class Qian_Cheng_Dai(unittest.TestCase):
    def setUp(self):
        # 登录
        self.login_url = 'http://120.78.128.25:8766/futureloan/member/login'
        # 充值
        self.recharge_url = 'http://120.78.128.25:8766/futureloan/member/recharge'

        self.login_headers = {'X-Lemonban-Media-Type': 'lemonban.v2',
                        'Content-Type': 'application/json'}
        self.token_headers = {'Authorization':self.test_login_01().json()['data']['token_info']['token']}

    def get_headers(self): # 请求头，包括token
        headers=self.login_headers.copy()
        headers.update(self.token_headers)

        return headers

    def tearDown(self):
        pass

    def test_login_01(self): # 正常登录
        data = {"mobile_phone": "18535653506",
                "pwd": "python123"}

        res = HttpRequest().http_request(method='post',url=self.login_url,data=json.dumps(data),headers = self.login_headers,cookies=None)
        try:
            self.assertEqual("18535653506",res.json()['data']['mobile_phone'])
            self.assertEqual(0,res.json()['code'])
        except AssertionError as e:
            raise e
        return res

    def test_login_02(self): # 手机号为空
        data = {"mobile_phone": "",
                "pwd": "python123"}

        res = HttpRequest().http_request(method='post',url=self.login_url,data=json.dumps(data),headers = self.login_headers,cookies=None)
        try:
            self.assertEqual("手机号码为空",res.json()['msg'])
        except AssertionError as e:
            raise e

    def test_login_03(self): # 手机号为3位
        data = {"mobile_phone": "123",
                "pwd": "python123"}

        res = HttpRequest().http_request(method='post',url=self.login_url,data=json.dumps(data),headers = self.login_headers,cookies=None)
        try:
            self.assertEqual("无效的手机格式",res.json()['msg'])
            self.assertEqual(2,res.json()['code'])
        except AssertionError as e:
            raise e

    def test_recharge_01(self): # 正常充值
        data = {
                "member_id":self.test_login_01().json()['data']['id'],
                "amount": "300"
                }
        res = HttpRequest().http_request('post',self.recharge_url,data=json.dumps(data),headers = self.get_headers())
        try:
            self.assertEqual("18535653506",res.json()['data']['mobile_phone'])
        except AssertionError as e:
            raise e
    def test_recharge_02(self): # 充值金额为负数
        data = {
                "member_id":self.test_login_01().json()['data']['id'],
                "amount": "-1"
                }
        res = HttpRequest().http_request('post',self.recharge_url,data=json.dumps(data),headers = self.get_headers())
        try:
            self.assertEqual("余额必须大于0并且小于或者等于500000",res.json()['msg'])
        except AssertionError as e:
            raise e

if __name__ == '__main__':
    unittest.main()
