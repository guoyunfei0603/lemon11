# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 14:53
# @Author  : guoyunfei.0603
# @File    : __init__.py.py
import openpyxl

a = openpyxl()
import requests

url = "http://120.78.128.25:8766/futureloan/member/login"

payload = "{\r\n  \"mobile_phone\": \"15815541764\",\r\n  \"pwd\": \"lemon666\"\r\n}"
headers = {
  'X-Lemonban-Media-Type': 'lemonban.v2',
  'Content-Type': 'application/json',
  'Content-Type': 'application/json',
  'Cookie': 'remember_me=18684720553'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
