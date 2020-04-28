"""
需求变更：
1.2 把某列的数据取出来
1.3 把某单元格的数据取出来
1.4 把所有数据读取出来，但是不读取标题
"""
import xlrd


def col():

    bk = xlrd.open_workbook(r"D:\TEST\公司信息.xlsx")
    sheet = bk.sheet_by_name("头条")

    col_values = sheet.col_values(6,7)

    print(col_values)

# col()


def cell():
    bk = xlrd.open_workbook(r"D:\TEST\公司信息.xlsx")
    sheet = bk.sheet_by_name("头条")

    cell_value = sheet.cell_value(7,9)
    print(cell_value)

# cell()

def all():
    bk = xlrd.open_workbook(r"D:\TEST\公司信息.xlsx")
    sheet = bk.sheet_by_name("头条")


    # row_values =sheet.row_values(7,6)
    # print(row_values)

# 定义一个空列表来存储读取到的所有数据
    all_row = []
    for i in range(7,11):  # 找规律，变的是行，从7开始，  7，8，9
        all_row.append(sheet.row_values(i,6))  # 把读取到的每一行数据添加到空列表里面
    print(all_row)


all()




