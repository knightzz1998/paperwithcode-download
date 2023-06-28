#! /usr/bin/env python
# -*-coding:utf-8-*-

from openpyxl import Workbook


def write_excel(datas, filename):
    # 创建一个新的Excel工作簿
    workbook = Workbook()
    # 获取活动的工作表
    worksheet = workbook.active
    # 写入字典的键作为表头
    data_dict = ['标题', '摘要', '中文摘要', '论文主页', 'pdf链接', 'github代码']
    headers = list(data_dict)
    worksheet.append(headers)

    for data_dict in datas:
        # 写入字典的值
        values = list(data_dict.values())
        worksheet.append(values)
    # 保存Excel文件
    workbook.save(filename)
