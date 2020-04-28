# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 18:21
# @Author  : guoyunfei.0603
# @File    : test_browser.py

class Browser:
    def __init__(self):
        self.name = "公共浏览器"



    def openUrl(self):
        print("打开浏览器"+self.name)

    def close(self):
        print("关闭公共的浏览器")