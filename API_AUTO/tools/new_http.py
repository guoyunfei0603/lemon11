import requests

requests.packages.urllib3.disable_warnings()  # 移除安全证书警告
import json

class HttpRequest:
    """
    利用requests封装成get 请求和 post 请求
    """

    def http_request(self,method,url,data,headers = None,cookies=None):
        """
        url：请求的地址 http://xxx:port
        :param: 传递的参数，非必填参数 字典的格式传递参数
        :return:
        """
        if method.lower() == 'get':
            res = requests.get(url,data,headers=headers,cookies=cookies)
        else:
            res = requests.post(url,data,headers=headers,cookies=cookies)
            # 注意：如果Content-Type类型是json 那么需要序列化，导入json包  json.dumps(data)

        return res
# if __name__ == '__main__':
    # url = 'http://120.78.128.25:8766/futureloan/member/login'
    #
    # headers = {'X-Lemonban-Media-Type': 'lemonban.v2',
    #            'Content-Type': 'application/json'}
    #
    # playload = {"mobile_phone": "18535653506",
    #             "pwd": "python123"}
    #
    # # res = HttpRequest().http_request(method='post',url=url,data=json.dumps(playload),headers = headers,cookies=None)
    # res = HttpRequest().http_request('post',url,json.dumps(playload),headers)
    # print(res.json())
