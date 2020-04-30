# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 16:45
# @Author  : guoyunfei.0603

# python两个字典合并
dict_1 = {'X-Lemonban-Media-Type': 'lemonban.v2',
        'Content-Type': 'application/json'}

dict_2 = {'Authorization':'Bearer Token'}

headers = dict_1.copy()
headers.update(dict_2)

# print(headers)

class Test_1:

        # def setUp(self):
        #         self.login_url = 'http://120.78.128.25:8766/futureloan/member/login'
        #         self.login_headers = {'X-Lemonban-Media-Type': 'lemonban.v2',
        #                               'Content-Type': 'application/json'}
        #         self.token_headers = {'Authorization': self.test_login_01()}


        def get_headers(self):
                self.login_headers = {'X-Lemonban-Media-Type': 'lemonban.v2',
                                      'Content-Type': 'application/json'}
                self.token_headers = {'Authorization':'21313'}

                headers = self.login_headers.copy()
                headers.update(self.token_headers)

                print(headers)
t = Test_1()
t.get_headers()

