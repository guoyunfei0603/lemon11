import xlrd

"""
变成类
"""
class My_Exlce():
    def __init__(self):
        # 做成受保护的,不想对外暴露属性
        self._path = ""
        self._sheet_name = ""

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self,path):
        self._path=path

    @property
    def sheet_name(self):
        return self._sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        self._sheet_name = sheet_name

    def sheet_init(self):
        bk = xlrd.open_workbook(self._path)
        sheet = bk.sheet_by_name(self._sheet_name)

        return sheet

    # 获取总行数
    def total_row(self):

        return self.sheet_init().nrows  # nrws 是在sheet类里面



    # 读某行
    def row(self,row_num,start_col,end=None):

        row_values = self.sheet_init().row_values(row_num,start_col)
        return row_values


    # 读某列
    def col(self,col_num,strat_row,end=None):
        col_values = self.sheet_init().col_values(col_num,strat_row)

        return col_values


    # 读某单元格字段
    def cell(self,row_num,col_num):

        cell_value = self.sheet_init().cell_value(row_num,col_num)
        return cell_value


    # 读指定列的所有
    def all(self,col_num,start_row_num, end_row_num=None):
        all_row = []
        if end_row_num ==None:
            end_row_num == self.total_row()  # 记住是用self.

        for i in range(start_row_num, end_row_num):  # 找规律，变的是行，从7开始，  7，8，9
            all_row.append(self.sheet_init().row_values(i,col_num ))  # 把读取到的每一行数据添加到空列表里面
        return all_row


# 创建对象
my = My_Exlce()

# 静态属性
# my._path = r"D:\TEST\公司信息.xlsx"  # 这样直接调用也可以，但是不推荐，用get和set方法  @property
# my._sheet_name = "头条"

# 封装后，通过对象.属性调用
my.path = r"D:\TEST\公司信息.xlsx"  # 把方法当属性用
my.sheet_name = "头条"

# 测试
read_row = my.row(7,7)
print(read_row)

print(my.col(8,9))

print(my.all(6,7,11))

print(my.total_row())