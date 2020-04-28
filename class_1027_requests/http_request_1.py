# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 14:07
# @Author  : guoyunfei.0603
# @File    : http_request_1.py

import requests
requests.packages.urllib3.disable_warnings()  # 移除安全证书警告

def ketangpai():
    url = 'https://www.baidu.com'
    res = requests.get(url,verify=False) # 返回一个消息实体
    print(res)
    # 响应头，响应状态码  响应报文 -->>全部封装在消息实体里面
    print('响应头',res.headers)
    print('响应状态码',res.status_code)
    print('响应报文',res.text)
    print('请求的header',res.request.headers)
    return res.cookies

# 如果响应报文是html 用--》text
# 如果响应报文是josn 用--》json()
# ketangpai()


# 登录
def login():
    url = 'https://www.ketangpai.com/UserApi/login'
    data= {'email': '18535653506',
            'password':'gyf3803628',
            'remember': 0}

    res = requests.post(url, json=data,verify=False) # 忽略HTTPS  verify=False
    print('响应正文1：',res.text)
    print('响应正文2：',res.json())
    print('响应头',res.headers)
    print('响应状态码',res.status_code)
    print('响应报文',res.text)
    print('——————cookies——————',res.cookies)

# login()
# 测试过程中，登录遇到 图片验证码，短信验证码怎么办？
"""
1. 找开发屏蔽他
2. 万能的验证码
3. 数据库查实时的验证码
4. 手动填 
"""