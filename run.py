#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/27 16:07
# @Author : shlu
# @Site : 
# @File : run.py
# @Software: PyCharm
import pytest
import os

if __name__ == '__main__':

    #--alluredir这个选项，用于指定存储测试结果的路径，在当前目录下的allure-result目录
    #--clean-alluredir：清空上一次的测试数据
    pytest.main(['-s','-q','test_pms.py','--alluredir','./allureDemo-result','--clean-alluredir'])
    #allureDemo generate：使用测试数据生成测试报告，放在当前目录下的reports目录
    #--clean：清空上一次的html报告
    #./allureDemo-result表示测试数据的所在目录（表示执行测试后json数据的输出目录）
    #-o 表示output 输出
    #./reports表示html报告所在目录
    os.system('allure generate ./allureDemo-result -o ./reports --clean')