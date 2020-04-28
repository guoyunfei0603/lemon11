"""
读取excel 安装xlrd第三方库  pip install xrld

需求：读取指定目录下表格内的一行信息   path = r“D:\TEST\公司信息.xlsx”

Alt+7 显示当前类下面的函数、属性


"""
# sheet_name = bk.sheet_names()      # 获取所有表格 ['Sheet1', 'Sheet2', 'Sheet3']


# 第一参数很重要
# 打开文件
import xlrd # 2. 导包 Alt+Shift+Enter

# 1. open_workbook（百度查到的）
bk = xlrd.open_workbook(filename=r"D:\TEST\公司信息.xlsx") # 显式的传参

"""
3. 跟踪代码，按住ctrl键不动，点击要跟踪的代码
    3.1 发现是个函数 open_workbook
        （1）看是否有返回值return  如果有，马上用一个变量去接收返回
        （2）再看有哪些参数，如果有必填参，就一定要传入，选填参数根据实际来决定
"""
# 4. 我打印这个返回到底是什么？？至少可以判断这行有没有问题
# print(bk)  # <xlrd.book.Book object at 0x000002C07454E3C8> 返回的是一个对象，


# 5. 这个Book是在哪找？ class Book（BaseObject）
           # 那么问题来了，怎么找这个bk？ bk是什么？？
           # 跟代码 bk是一个对象，Book类的对象  ，所以可以调用Book里面的方法， bk.

# 调用静态属性，类名.    对象.

# 6. 我下面的代码都是托管给了bk，一定是bk.出来的，既然是这样，我就要研究一下Book类到底有什么？

# 7. 打开我要读取的那个sheet

# print(bk.nsheets)   # 我总共有多少个sheet

# 我已经得到这个方法了，看有没有返回，  有 用变量接收一下，打印出来

# sheets = bk.sheets()   # 跟代码发现，sheet是sheet的对象

# print(sheets)
# [<xlrd.sheet.Sheet object at 0x000001DF35FAE908>,
# <xlrd.sheet.Sheet object at 0x000001DF35E61808>,
# <xlrd.sheet.Sheet object at 0x000001DF35FCE608>,
# <xlrd.sheet.Sheet object at 0x000001DF35FCE948>]
# 相当于拿到所有sheet表的下标

# 获取所有book下的sheet名
# sheet_name = bk.sheet_names()
# print(sheet_name)  # ['头条', 'test', 'Sheet3', 'Sheet4']


"""
7. 
bk.sheet_by_name("头条") 找到指定的工作表，有返回用sheet接收

sheet是对象，可以调用sheet类里面的方法
"""
sheet = bk.sheet_by_name("头条")
print(sheet)

# 8. 跟踪sheet 发现是Sheet类的对象，研究Sheet里面有那些方法
row = sheet.row_values(7,6)
print(row)

# print(sheet.row(2))   # 整行都打印


