# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 18:42
# @Author  : gyf

"""
写一个课堂派的登录，正确的、手机号错误、密码为空、
加上异常处理和断言
"""

import requests
import unittest
requests.packages.urllib3.disable_warnings()
from class_1101.API_AUTO.http_request import HttpRequest
from class_1101.teacher_homework.fanshe import GetData

# cookie 有没有更好的处理方式？
# 面试官可能会问，两个接口，第二个接口用到第一个接口返回的参数
# 1. 全局变量  缺点：关联性很强，一步错，步步错
# 2. 反射(能掌握最好)     缺点：关联性很强，一步错，步步错
# 3. 登录写到setUp里面
"""
我没做出来，全局变量和反射报错
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
以后再改吧
"""
# COOKIE = None

class Test_KeTangPai(unittest.TestCase):
    def setUp(self):
        # 登录的url
        self.login_url = 'https://www.ketangpai.com/UserApi/login'
        # 评论的url
        self.common_url = 'https://www.ketangpai.com/TopicDiscussApi/addDiscuss'
        # 删除评论的url
        self.del_common_url = 'https://www.ketangpai.com/TopicDiscussApi/delDiscuss'


    def test_login_01(self): # 正常登录
        # global COOKIE # 声明全局变量
        # 如果你要在局部修改全局变量，必须声明

        data = {"email": "18535653506",
                "password": "gyf3803628",
                "remember": 0}

        res = HttpRequest().http_requests(self.login_url, data, "post")
        if res.cookies:
            # COOKIE = res.cookies
            setattr(GetData,'Cookie',res.cookies) # 利用反射
        else:
            print("cooke 获取失败")

        try:
            self.assertEqual(1,res.json()['status']) # 断言status=1
        except AssertionError as e:
            raise e  # 抛出异常

    def test_login_02(self): # 手机号错误

        data = {"email": "123456",
                "password": "gyf3803628",
                "remember": 0}

        res = HttpRequest().http_requests(self.login_url, data, "post")
        try:
            self.assertEqual("用户不存在",res.json()['info'])
        except AssertionError as e:
            raise e


    def test_login_03(self): # 密码为空
        data = {"email": "18535653506",
                "password": "",
                "remember": 0}

        res = HttpRequest().http_requests(self.login_url, data, "post")
        try:
            self.assertEqual("密码不能为空aaaaa",res.json()['info'])
        except AssertionError as e:
            raise e



    def test_common_01(self):# 发表评论
        # global COOKIE

        data = {'topicid':'MDAwMDAwMDAwMLSGpZmHubuv',
                'content':'测试发表评论~~',
                'anonymous':0}
        # res = HttpRequest().http_requests(self.common_url,data,"post",COOKIE)
        res = HttpRequest().http_requests(self.common_url, data, "post", getattr(GetData,'Cookie'))
        try:
            self.assertEqual("发表成功",res.json()['info'])
        except AssertionError as e:
            raise e

        return res.json()['data']['id']  # 拿到评论后的id

    def test_del_common_01(self): # 删除已发表的评论
        global COOKIE

        data = {'id':self.test_common_01()}
        res = HttpRequest().http_requests(self.del_common_url,data,'post',getattr(GetData,'Cookie'))

        try:
            self.assertEqual("success",res.json()['info'])

        except AssertionError as e:
            raise e

    def test_del_comon_02(self): # 删除别人的评论--无权限
        global COOKIE
        data = {'id': 123}
        res = HttpRequest().http_requests(self.del_common_url, data, 'post', getattr(GetData,'Cookie'))

        try:
            self.assertEqual("你没有权限删除别人的评论", res.json()['info'])
        except AssertionError as e:
            raise e


    def tearDown(self):
        pass

if __name__ == '__main__':
    r = Test_KeTangPai().test_common_01()
    print(r)


    
