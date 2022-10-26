#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022/10/25 14:32
# @Author : 梁灿

"""
缓存文件处理
"""
import os
from typing import Any, Text, Union
from common.setting import ensure_path_sep

class Cache:
    """设置读取缓存"""
    def __init__(self, filename: Union[Text, None]) -> None:
        # 如果filename不为空，则操作指定文件内容
        if filename:
            self.path = ensure_path_sep("\\cache" + filename)
        # 如果filename为None，则操作所有文件内容
        else:
            self.path = ensure_path_sep("\\cache")
    def set_cache(self, key: Text, value: Any) -> None:
        """
        设置缓存，只支持设置单字典缓存数据，缓存文件如果已存在，则替换之前的缓存内容
        :param key:
        :param value:
        :return:
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(str({key: value}))

    def set_caches(self, value: Any) -> None:
        """
        设置多组缓存数据
        :param value: 缓存内容
        :return:
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(str(value))

    def get_cache(self) -> Any:
        """
        获取缓存数据
        :return:
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            pass

    def delete_cache(self) -> None:
        """删除所有缓存文件"""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"你要删除的缓存文件不存在 {self.path}")
        os.remove(self.path)

    @classmethod
    def clean_all_cache(cls) -> None:
        """
        清楚所有缓存文件
        :return:
        """
        cache_path = ensure_path_sep("\\cache")

        # 列出目录下所有文件，生成一个list
        list_dir = os.listdir(cache_path)
        for i in list_dir:
            # 循环清楚文件夹下的所有内容
            os.remove(cache_path + i)


_cache_config = {} #生成一个缓存配置字典

class CacheHandler:
    @staticmethod
    def get_cache(cache_data):
        return _cache_config[cache_data]

    @staticmethod
    def update_cache(*,cache_name, value):
        _cache_config[cache_name] = value




