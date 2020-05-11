# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 19:07
# @Author  : guoyunfei.0603

from openpyxl import load_workbook

class Demo_Excel:
    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def get_data(self):
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]

        test_data = []
        for item in range(2,sheet.max_row+1):
            sub_data = {}

            sub_data['url'] = sheet.cell(item,1).value
            sub_data['data'] = sheet.cell(item,2).value
            sub_data['expected'] = sheet.cell(item,3).value
            sub_data['method'] = sheet.cell(item,4).value
            test_data.append(sub_data)
        return test_data


if __name__ == '__main__':
    test_data = Demo_Excel('Demo.xlsx','Sheet1').get_data()
    print(test_data)
