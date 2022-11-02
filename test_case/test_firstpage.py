#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-10-26 21:10:54


import allure
import pytest
from lib.read_files_tools.get_yaml_data_analysis import GetTestCase
from lib.assertion.assert_control import Assert
from lib.requests_tools.request_control import RequestControl
from lib.read_files_tools.regular_control import regular
from lib.requests_tools.teardown_control import TearDownHandler


case_id = ['login_01']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("立友接口")
@allure.feature("首页模块")
class TestLogin:

    @allure.story("首页")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_login(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
