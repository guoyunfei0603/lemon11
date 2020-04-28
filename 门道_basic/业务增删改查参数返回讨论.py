# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 14:25
# @Author  : guoyunfei.0603
# @File    : 业务增删改查参数返回讨论.py

# 增加
# 【无参无返回】
# 如果你想区分选填必填等,就改造成[有参无返回]
def insertUser():
    # username = 界面接收到的username
    # pwd = 界面接收到的pwd
    # ...
    # user：表名
    pass # insert into user (username,pwd,...) values ("测试",123456,...)

# 删除
# 【有参无返回】
# 如果你想看看有没有删除，也可以改为[有参有返回]
def deleteUser(userid):
    # userid = 界面输入的userid
    pass # delete from user where uid = userid

# 修改:  编辑,提交
# 1. 编辑【有参有返回】
def editUser(userid):
   rs = []
   # rs = select * from user where uid = userid
   return rs
# 2. 提交【无参无返回】
def updateUser():
    pass

# 查询
# 1. 根据条件查询部分选项【有参有返回】
def selectUser(name):
    rs=[]
    # rs = select * from user where username = name
    return rs
# 2. 查询所有【无参有返回】
def index():
    rs = []
    return rs
