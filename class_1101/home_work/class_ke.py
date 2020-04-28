# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 18:42
# @Author  : gyf

"""
写一个课堂派的登录，正确的、手机号错误、密码为空、
加上异常处理和断言
"""
import requests
import unittest

from class_1101.teacher_homework.fanshe import GetData

requests.packages.urllib3.disable_warnings()
from class_1101.API_AUTO.http_request import HttpRequest


class Test_KeTangPai(unittest.TestCase):
    def setUp(self):
        pass

    def test_login_01(self): # 正常登录
        url = 'https://www.ketangpai.com/UserApi/login'

        data = {"email": "18535653506",
                "password": "gyf3803628",
                "remember": 0}

        res = HttpRequest().http_requests(url, data, "post")

        try:
            self.assertEqual(1,res.json()['status']) # 断言status=1
        except AssertionError as e:
            raise e  # 抛出异常

        return res.cookies


    def test_login_02(self): # 手机号错误
        url = 'https://www.ketangpai.com/UserApi/login'

        data = {"email": "123456",
                "password": "gyf3803628",
                "remember": 0}

        res = HttpRequest().http_requests(url, data, "post")
        try:
            self.assertEqual("用户不存在",res.json()['info'])
        except AssertionError as e:
            raise e

        return res.json()

    def test_login_03(self): # 密码为空
        url = 'https://www.ketangpai.com/UserApi/login'

        data = {"email": "18535653506",
                "password": "",
                "remember": 0}

        res = HttpRequest().http_requests(url, data, "post")
        try:
            self.assertEqual("密码不能为空aaaaa",res.json()['info']) # 错误示例
        except AssertionError as e:
            raise e

        return res.json()


    def test_common_01(self):# 发表评论
        url = 'https://www.ketangpai.com/TopicDiscussApi/addDiscuss'
        data = {'topicid':'MDAwMDAwMDAwMLSGpZmHubuv',
                'content':'测试发表评论~~',
                'anonymous':0}
        res = HttpRequest().http_requests(url,data,"post",cookie=self.test_login_01())
        try:
            self.assertEqual("发表成功",res.json()['info'])
        except AssertionError as e:
            raise e

        return res.json()['data']['id']  # 拿到评论后的id

    def test_del_common_01(self): # 删除已发表的评论
        url = 'https://www.ketangpai.com/TopicDiscussApi/delDiscuss'
        data = {'id':self.test_common_01()}
        res = HttpRequest().http_requests(url,data,'post',cookie=self.test_login_01())

        try:
            self.assertEqual("success",res.json()['info'])
        except AssertionError as e:
            raise e

        return res.json()

    def test_del_comon_02(self): # 删除别人的评论--无权限

        url = 'https://www.ketangpai.com/TopicDiscussApi/delDiscuss'
        data = {'id': 123}
        res = HttpRequest().http_requests(url, data, 'post', cookie=self.test_login_01())

        try:
            self.assertEqual("你没有权限删除别人的评论", res.json()['info'])
        except AssertionError as e:
            raise e

        return res.json()

    def tearDown(self):
        pass

if __name__ == '__main__':
    r = Test_KeTangPai().test_login_01()
    print(r)