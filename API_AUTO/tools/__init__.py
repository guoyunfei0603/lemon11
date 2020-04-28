# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 16:04
# @Author  : guoyunfei.0603
# @File    : __init__.py.py
import requests

# gogokid 家长端登录
url = 'https://www.gogokid.com/passport/web/user/login/?account_sdk_source=web'
data = {
'account':'18503959675',
'password':'123456',
'region':'CN',
'aid':1277,
'language':'zh'
}

res = requests.post(url,data,verify = False)
print(res.json())
print(res.cookies)

# 任重而道远啊 cookies，到下个接口一直不行
