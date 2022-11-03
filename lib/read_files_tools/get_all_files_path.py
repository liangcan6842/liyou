#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time   : 2022/10/23 21:24
# @Author : 梁灿
"""
import os

def get_all_files(file_path,yaml_data_switch=False) -> list:
    """
    获取文件路径
    :param file_path: 目录路径
    :param yaml_data_switch: 是否过滤文件为yaml格式，True为过滤
    :return:
    """
    filename = []
    # 获取所有文件 下的文件名称
    for root,dirs,files in os.walk(file_path):
        for _file_path in files:
            path = os.path.join(root,_file_path)
            if yaml_data_switch:
                if 'yaml' in path or '.yml' in path:
                    filename.append(path)
            else:
                filename.append(path)
    return filename






















