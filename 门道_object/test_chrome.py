# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 18:29
# @Author  : guoyunfei.0603
# @File    : test_chrome.py
from 门道_object import test_browser
from 门道_object.class_object3 import Teacher

class Chrome(test_browser.Browser):


    def __init__(self):
        super().__init__()
        self.static = None

    def close(self):
        super(Chrome, self).close()

        super(Chrome,)
        print("关闭谷歌浏览器")

    def getTitle(self):
        pass

class Firefox:

    def close(self):

        print("关闭火狐浏览器")

    def getTitle(self):
        pass

c = Chrome()
c.close()

c.static
