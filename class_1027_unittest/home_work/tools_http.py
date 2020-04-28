# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 21:31
# @Author  : guoyunfei.0603

import requests


requests.packages.urllib3.disable_warnings()  # 移除安全证书警告





class Http_Request():
    """
    利用requests封装成get 请求和 post 请求
    """
    def http_request(self,menthod,url,data,cookie=None):
        if menthod == 'get':
            res = requests.get(url,data,cookie)
        else:
            res = requests.post(url,data,cookie)
        return res

if __name__ == '__main__':
    url = 'http://154.221.31.241:8080/admin/member/manage/login'
    data = {'mobile':'18535653506',
            'password':'123456'}

    res = Http_Request().http_request('post',url,data)
    print(res.json())