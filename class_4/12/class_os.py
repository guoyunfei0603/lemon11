# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 21:37
# @Author  : guoyunfei.0603
# @File    : class_os.py

import os

dirs = r'D:\工作内容资料\测试用例'
listdirs = os.listdir(dirs)
# print(listdirs) # 打印目录下的所有文件和文件夹

#
# print(os.path.join(dirs,listdirs[0]))


# isfile = os.path.isfile(os.path.join(dirs,listdirs[0]))
