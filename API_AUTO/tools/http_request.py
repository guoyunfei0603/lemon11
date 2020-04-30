# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 16:05
# @Author  : guoyunfei.0603
# @File    : http_request.py

import requests
import json
requests.packages.urllib3.disable_warnings()  # 移除安全证书警告

class HttpRequest:
    """
    利用requests封装成get 请求和 post 请求
    """

    def http_request(self,url,data,method,cookies=None):
        """
        url：请求的地址 http://xxx:port
        :param: 传递的参数，非必填参数 字典的格式传递参数
        :return:
        """
        if method.lower() == 'get':
            res = requests.get(url,data,cookies=cookies)
        else:
            res = requests.post(url,data,cookies=cookies)
            # 注意：如果Content-Type类型是json 那么需要序列化，导入json包  json.dumps(data)

        return res
# if __name__ == '__main__':
#     url = 'http://120.78.128.25:8766/futureloan/member/login'
#
#     data = {
#         "mobile_phone": "18535653506",
#         "pwd": "python123"
#
#     }
#
#     headers = {'X-Lemonban-Media-Type': 'lemonban.v2',
#                'Content-Type': 'application/json'}
#     res = HttpRequest().http_request(url,json.dumps(data),'post',headers)
#     print(res.text)
