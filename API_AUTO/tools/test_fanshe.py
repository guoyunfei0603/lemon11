# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 22:16
# @Author  : guoyunfei.0603

# 反射
class GetData:
    Cookie = None # 存储cookie，初始值为None

# # setattr 和 getattr 最常用,例如：
# setattr(GetData,'Cookie','abc123456789') # 修改类里面的属性值
# print(getattr(GetData,'Cookie')) # 获取Cookie