# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 21:06
# @Author  : gyf

# 反射
class GetData:
    Cookie = None # 存储cookie，初始值为None


# 示例：
# class GetData:
#     Cookie = 'ABCD666'
#
# print('未修改的cookie值是：   ',GetData.Cookie) # 打印Cookie值
#
# # setattr 和 getattr 最常用
# setattr(GetData,'Cookie','abc123456789') # 修改类里面的属性值
# print(getattr(GetData,'Cookie')) # 获取Cookie
#
# print(hasattr(GetData,'Cookie')) # 判断类里面是否有Cookie
#
#
#
# print('修改后的cookie值是：',GetData.Cookie)

# delattr(GetData,'Cookie')  # 删除属性  --不常用
# print(getattr(GetData,'Cookie'))



