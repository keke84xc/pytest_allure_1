#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/27 15:03
# @Author : shlu
# @Site : 
# @File : load_yaml_data.py
# @Software: PyCharm
import yaml
import os

def get_yaml_data(filename):

    #print(os.getcwd())

    if "config" in os.getcwd():
        # 项目根目录
        path1 = os.path.dirname(os.path.dirname(__file__))
    else:
        path1 = os.getcwd()

    yaml_file_path = os.path.join(path1,'data',filename)
    #D:/testKits/git_repository/pytest_allure_1\data\login.yaml
    print(yaml_file_path)
    s = open(yaml_file_path,mode='r')
    data = yaml.load(s,yaml.FullLoader)

    print(data)

    return data

if __name__ == '__main__':
    get_yaml_data('login.yaml')