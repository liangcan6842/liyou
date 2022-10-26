#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022/10/21 18:88
# @Author : 梁灿
"""
断言类型封装，支持json断言、数据库断言
"""
import ast,json
from typing import Text,Dict,Any,Union
from jsonpath import jsonpath
from lib.logging_tools.log_control import ERROR,WARNING
from lib.read_files_tools.regular_control import cache_regular
from lib.other_tools.models import load_module_functions
from lib.assertion import assert_type
from lib.other_tools.exceptions import JsonpathExtractionFailed,SqlNotFound,AssertTypeError
from lib import config


class Assert:
    """assert 模块封装"""
    def __init__(self,assert_data:Dict):
        self.assert_data = ast.literal_eval(cache_regular(str(assert_data)))
        self.functions_mapping = load_module_functions(assert_type)

    @staticmethod
    def _check_params(
            response_data: Text,
            sql_data: Union[Dict, None]) -> bool:
        """

        :param response_data: 响应数据
        :param sql_data: 数据库数据
        :return:
        """
        if (response_data and sql_data) is not False:
            if not isinstance(sql_data,dict):
                raise ValueError(
                    "断言失败，response_data、sql_data的数据类型必须要是字典类型，"
                    "请检查接口对应的数据是否正确\n"
                    f"sql_data: {sql_data}, 数据类型: {type(sql_data)}\n"
                )
        return True

    @staticmethod
    def res_sql_data_bytes(res_sql_data: Any) -> Text:
        """处理mysql查询出来的数据类型，如果是bytes类型，转化成str类型"""
        if isinstance(res_sql_data,bytes):
            res_sql_data = res_sql_data.decode('utf-8')
        return res_sql_data

    def sql_switch_handle(
            self,
            sql_data: Dict,
            assert_value: Any,
            key: Text,
            values: Any,
            resp_data: Dict,
            message: Text) -> None:
        """

        :param sql_data: 测试用例中的sql
        :param assert_value: 断言内容
        :param key:
        :param values:
        :param resp_data: 预期结果
        :param message: 预期结果
        :return:
        """
        # 判断数据库开关为关闭状态
        if config.mysql_db.switch is False:
            WARNING.logger.warning(
                "检测数据库状态为关闭状态，程序已为你跳过此断言，断言值:%s", values
            )
        # 判断数据库为开启状态
        if config.mysql_db.switch:
            # 走正常的SQL短言逻辑
            if sql_data != {'sql':None}:
                res_sql_data = jsonpath(sql_data,assert_value)
                if res_sql_data is False:
                    raise JsonpathE

































