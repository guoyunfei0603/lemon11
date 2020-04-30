# @Time    : 2020/4/30 14:15
# @Author  : guoyunfei.0603
from requests import request
import json

url = 'http://120.78.128.25:8766/futureloan/member/login'

data = {
    "mobile_phone": "18535653506",
     "pwd": "python123"

    }

headers = {'X-Lemonban-Media-Type':'lemonban.v2',
            'Content-Type':'application/json'}

# 如果Content-Type类型是json 那么需要序列化
r = request('post', url, data=json.dumps(data),headers = headers)
print(r.text.encode('utf-8'))