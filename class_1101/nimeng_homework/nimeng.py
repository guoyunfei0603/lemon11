# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 20:57
# @Author  : gyf

from class_1101.API_AUTO.http_request import HttpRequest
import requests
import unittest

from class_1101.teacher_homework.fanshe import GetData



class NingMeng(unittest.TestCase):
    def setUp(self):
        self.login_url = 'http://154.221.31.241:8080/admin/member/manage/login'
        self.job_url = 'http://154.221.31.241:8080/admin/recruit/manage2/lists'
    def tearDown(self):
        pass

    def test_login_01(self):# 正常登录
        data = {'mobile':'18535653506',
                'password':'123456'}

        res = HttpRequest().http_requests(self.login_url,data,'post')
        if res.json()['data']['loginUuid']:
            setattr(GetData,'loginUuid',res.json()['data']['loginUuid'])

        try:
            self.assertEqual("登录成功",res.json()['msg'])
        except AssertionError as e:
            raise e

        # return res.json()['data']['loginUuid']

    def test_login_02(self):# 手机号为空
        data = {'mobile':'',
                'password':'123456'}

        res = HttpRequest().http_requests(self.login_url,data,'post')
        try:
            self.assertEqual("手机号码必须",res.json()['msg'])
        except AssertionError as e:
            raise e

    def test_login_03(self):# 密码错误
        data = {'mobile':'18535653506',
                'password':'123123123'}

        res = HttpRequest().http_requests(self.login_url,data,'post')
        try:
            self.assertEqual("帐号或密码错误?",res.json()['msg'])
        except AssertionError as e:
            raise e


    def test_select_job(self):# 查询岗位
        # data = {'loginUuid':self.test_login_01(),
        data = {'loginUuid':getattr(GetData,'loginUuid'), # 利用反射
                'offset':0,
                'limit':10}

        res = HttpRequest().http_requests(self.job_url,data,'post') # 缺点，这个接口不需要cookie
        return res.json()

