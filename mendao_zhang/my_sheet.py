import xlrd

"""
封装成函数
"""

# 读某行
def row(path,sheet_name,row_num,start_col,end=None):
    bk = xlrd.open_workbook(path)
    sheet = bk.sheet_by_name(sheet_name)
    row_values = sheet.row_values(row_num,start_col)
    return row_values


# 读某列
def col(path,sheet_name,col_num,strat_row,end=None):
    bk = xlrd.open_workbook(path)
    sheet = bk.sheet_by_name(sheet_name)

    col_values = sheet.col_values(col_num,strat_row)

    return col_values


# 读某单元格字段
def cell(path,sheet_name,row_num,col_num):
    bk = xlrd.open_workbook(path)
    sheet = bk.sheet_by_name(sheet_name)

    cell_value = sheet.cell_value(row_num,col_num)
    return cell_value


# 读指定列的所有
def all(path,sheet_name,start_row_num, end_row_num,col_num):
    bk = xlrd.open_workbook(path)
    sheet = bk.sheet_by_name(sheet_name)

    all_row = []
    for i in range(start_row_num, end_row_num):  # 找规律，变的是行，从7开始，  7，8，9
        all_row.append(sheet.row_values(i,col_num ))  # 把读取到的每一行数据添加到空列表里面
    return all_row


path = r"D:\TEST\公司信息.xlsx"
sheet_name = "头条"
row_num = 8
start_col = 6


read_row = row(path,sheet_name,row_num,start_col)
print(read_row)

read_col = col(path,sheet_name,6,7)
print(read_col)

read_cell = cell(path,sheet_name,8,8)
print(read_cell)

read_all = all(path,sheet_name,9,11,9)
print(read_all)
