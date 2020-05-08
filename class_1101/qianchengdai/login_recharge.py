# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:41
# @Author  : guoyunfei.0603
import requests
class HttpRequest:

    def http_request(self,method,url,data,json=None,cookies=None):
        if method.lower()=='get':
            resp=requests.get(url,params=data,cookies=cookies)
        elif method.lower()=='post':
            if json:
                resp=requests.post(url,json=json,cookies=cookies)
            else:
                resp=requests.post(url,data=data,cookies=cookies)
        else:
            print("method in not support")
        return resp

if __name__ == '__main__':
    t=HttpRequest()


    #注册接口调用
    # url='http://test.lemonban.com/futureloan/mvc/api/member/register'
    # data={"mobilephone": "18535653506", "pwd": "python123"}
    # resp=t.http_request('post',url,data)
    # print(resp.status_code)
    # print(resp.text)


    #登录接口调用
    url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    data={"mobilephone": "18535653506", "pwd": "python123"}
    resp=t.http_request('post',url,data)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)

    #充值接口调用
    data={"mobilephone": "18535653506", "amount": "10000"}
    url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    resp=t.http_request('post',url,data,cookies=resp.cookies)
    print(resp.status_code)
    print(resp.text)