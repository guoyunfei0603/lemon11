# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 16:58
# @Author  : gyf
import requests
requests.packages.urllib3.disable_warnings()
from class_1101.teacher_homework.fanshe import GetData

class HttpRequest:
    def http_request(self,url,data,method,cookie=None):
        """

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
    # 柠萌APP登录
    # url = 'http://154.221.31.241:8080/admin/member/manage/login'
    # data = {"mobile":"18535653506",
    #         "password":"123456"}
    #
    # res = HttpRequest().http_request(url,data,"post")
    # print(res.json())

    # 课堂派登录
    url = 'https://www.ketangpai.com/UserApi/login'

    data = {"email":"18535653506",
            "password":"gyf3803628",
           "remember":0}

    res = HttpRequest().http_request(url,data,"post")

    # print("课堂派的响应正文是：",res.json())
    # print("课堂派的cookie是：",res.cookies)

    # 发表评论
    url2 = 'https://www.ketangpai.com/TopicDiscussApi/addDiscuss'
    data2 = {'topicid':'MDAwMDAwMDAwMLSGpZmHubuv',
            'content':'测试发表评论~~',
            'anonymous':0}
    res2 = HttpRequest().http_request(url2,data2,"post",res.cookies)
    print(res2.json())
    # print("返回的id是：",res2.json()['data']['id'])

    res2_id = res2.json()['data']['id'] # 根据这个id删除评论

    # 删除发表的评论
    url3 = 'https://www.ketangpai.com/TopicDiscussApi/delDiscuss'
    data3 = {'id':res2_id}

    res3 = HttpRequest().http_request(url3,data3,"post",res.cookies)
    print(res3.json())



