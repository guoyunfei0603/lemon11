# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 10:03
# @Author  : guoyunfei.0603

import unittest
from unittest import mock
from requests import request


class TestPay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''请求第三方支付接口返回的数据'''
        url = 'http://docs.open.alipay.com/api 1 /alipay.trade.pay'
        data = {
            'user': 'kaishui',
            'pay_pwd': 123456,
            'money': 88.88
        }
        res_data = {
            'alipay_trade_response': {
                'tester': 'kaishui'
            },
            'sign': 'dwedwewecvvewvwre'
        }
        # 创建一个mock对象
        mock_res = mock.Mock(return_value=res_data)
        # 调用这个mock对象
        # 这里实际上并没有调用第三方接口，而是直接创建了一个mock对象request用来存放第三方接口返回的响应信息res_data。
        # 然后表面上是使用了request方法去请求，实际上只是直接返回了res_data的值
        cls.response = mock_res(url=url, data=data)

    def test_Pay(self):
        '''测试用例中需要用到前置条件支付接口返回的数据'''
        # 获取前置条件中支付返回的数据
        pay_res_data = self.response

if __name__ == '__main__':
    unittest.main()