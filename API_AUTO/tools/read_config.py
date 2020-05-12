# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 20:15
# @Author  : guoyunfei.0603

import configparser

class ReadConfig:
    def read_config(self,file_name,section_name,option):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section_name,option)


res = ReadConfig().read_config('case.config', 'MODE', 'mode')
print(res)