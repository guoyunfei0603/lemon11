# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 22:25
# @Author  : guoyunfei.0603
# @File    : class_os.py
import os
# os operate system 操作系统
# print(os.sep)      # 系统路径的分隔符  windows："\\"   linux："/"  mac：":"
# print(os.name)     # 正在使用的工作平台    windows："nt"   linux:"posix"
# print(os.getenv('JMETER_HOME'))    # 读取环境变量， 电脑-环境变量
# print(os.getcwd())                 # 获取当前的路径
#
#
#
#
# # 编写一个程序：在当前目录下查找文件名包含指定字符串的文件
cur_path = os.getcwd()
# 获取到当前目录下的所有文件
files = os.listdir(cur_path)
name = 'home'
for item in files:

    if os.path.isfile(item):
         if item.find(name) != -1:
             # Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
             # 则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
             print(os.path.join(cur_path,item))






# 判断是不是一个文件




#
# dirs = r'E:\test'
# # 列出该目录下的所有文件
# files = os.listdir(dirs)
# print(files)
# # 拼接了路径
# fullpath = os.path.join(dirs,files[-3])
# print(fullpath)
#
# if os.path.isfile(fullpath):
#     print('这是一个文件')
# elif os.path.isdir(fullpath):
#     print("这是一个目录")
#
#
# d = r'E:\test\demo'  # 没有才创建，而且要有判定条件
# # 判断目录是否存在
# if not os.path.exists(d):
#      os.makedirs(d)     # 创建目录

# rmdir() 只能删除空目录     
# os.rmdir(d)


# os.chdir()

# os.chdir("\\23")