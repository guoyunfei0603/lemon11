# @Time    : 2020/4/25 15:02
# @Author  : gyf

import requests
requests.packages.urllib3.disable_warnings()

class HttpRequest:
    def http_requests(self,url,data,method,cookie=None):
        """
        写一个封装get和post请求的类
        :param url:
        :param data:
        :param method:
        :param cookie:
        :return:
        """
        if method.lower() == 'get':
            res = requests.get(url,data,cookies = cookie,verify = False)
        else:
            res = requests.post(url,data,cookies = cookie,verify = False)
        return res

if __name__ == '__main__':
    pass