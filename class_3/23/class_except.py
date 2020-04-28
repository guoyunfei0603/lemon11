# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 23:45
# @Author  : guoyunfei.0603
# @File    : class_except.py

# 异常处理

# 第一种：  try...except
# try:
#     f = open('test_01.txt','a',encoding='utf-8')
#     f.read('我们都一样')
# except Exception as e:
#     print('****错误****',e)

# 第二种：  try...except...finally
try:
    f = open('test_01.txt','a',encoding='utf-8')
    f.read('我们都一样')
except Exception as e:     # 常用错误类：Exception ,  as相当于赋值给e
    print('****错误****',e)
finally:
    print('最终-------都要执行-----------')

# 第三种    try..except..else  不推荐
# try:
#     f = open('test_01.txt','a',encoding='utf-8')
#     f.write('我们都一样')
# except Exception as e:
#     print('****错误****',e)
# else:
#     print('try如果执行成功，我就执行')



print("\n程序正常执行---")