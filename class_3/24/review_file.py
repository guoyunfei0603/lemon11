# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 17:56
# @Author  : guoyunfei.0603
# @File    : review_file.py

# 1. 判断当前路径下E:\test\demo有没有文件夹“测试”，如果没有就创建文件夹：测试
# 2. 在测试文件夹里面创建一个test11.txt 写入内容"hello word！" 并返回绝对路径
import os
p = r"E:\test\demo\测试"
if not os.path.exists(p):
    os.makedirs(p)

os.chdir(p) # 指定到具体路径，切记！！！！
f=open("test11.txt",'a')
f.write("hello word!")

files=os.listdir(p) # 列出当前目录下的所有内容(文件夹/目录)
print(files)

try:
    if os.path.isfile(files[0]):
        print("这是一个文件路径",os.path.join(p,files[0]))
    elif os.path.isdir(files[1]): # 写的不好，
        print("这是一个目录")
except Exception as e:
    print("***错误日志***",e)

