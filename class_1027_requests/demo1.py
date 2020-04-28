# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 16:12
# @Author  : guoyunfei.0603
# @File    : demo1.py
import requests
requests.packages.urllib3.disable_warnings()  # 移除安全证书警告

def login():
    """
    url：请求的地址 http://xxx:port
    :param: 传递的参数，非必填参数 字典的格式传递参数
    :return:
    """
    url = 'https://www.ketangpai.com/UserApi/login'
    data = {'email': '18535653506',
            'password': 'gyf3803628',
            'remember': 0}

    res = requests.post(url, json=data, verify=False)  # 忽略HTTPS  verify=False
    return res.text # 返回一个消息实体，包括响应头，响应正文，cookie等

login = login()
print(login)

def add_comment(): # 发表评论
    url = 'https://www.ketangpai.com/TopicDiscussApi/addDiscuss'
    data = {"topicid":"MDAwMDAwMDAwMLSGpZmHubdr",
            "content":"测试",
            "anonymous":0}

    a = requests.post(url,data,verify = False,cookies = login())
    print(a.text)
# 没有跑通这个函数

# add_comment()