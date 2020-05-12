# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:18
# @Author  : guoyunfei.0603

import unittest
from API_AUTO.tools.http_request import HttpRequest
from API_AUTO.tools.test_fanshe import GetData
from ddt import ddt,data
from class_1103.test_excel_2.demo_excel import Demo_Excel

'''
用ddt方式  建议使用，  但是超继承的原理要懂，保留父类的属性方法，super
'''

test_data = Demo_Excel('Demo.xlsx', 'Sheet1').get_data([1,3]) # 传入列表['case_id'] 达到控制执行那几条用例

@ddt
class Qian_Cheng_Dai(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    @data(*test_data)
    def test_api(self,item):# 接口用例

        res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'],getattr(GetData,'Cookie'))
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)

        try:
            self.assertEqual(item['expected'],res.json()['msg'])
        except AssertionError as e:
            raise e

if __name__ == '__main__':
    unittest.main()


