# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 9:44
# @Author  : guoyunfei.0603
# @File    : home_work2.py
import os

# 写一个文件，内容："Hello Word！" 写入D:\\test\\01.txt路径下
# f = open("D:\\test\\01.txt",'w',encoding='UTF-8')  # 路径必须创建好
# f.write("Hello Word!!")
# f.close()

dirs = r'D:\test'
files = os.listdir(dirs)
print(files) # 返回一个列表 ['01.txt', '02.txt', '测试']
full_path= os.path.join(dirs,files[2]) # 拼接路径


if os.path.isfile(full_path):
    print("这是一个文件",full_path)
elif os.path.isdir(full_path):
    print("这是一个目录",os.path.join(dirs,full_path))  # 比较麻烦，直接full_path
    os.makedirs(r'D:\test\目录下创建')   #  
    print(os.getcwd(),"****当前的路径")
    os.chdir(r'D:\test\目录下创建')   # 移动指定位置
    f = open("巴拉巴拉.txt",'a')
    f.write("拍脑袋~~")
    f.close()



