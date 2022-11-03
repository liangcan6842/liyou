#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time   : 2022/10/26 17:10
# @Author : 梁灿
描述: 发送邮件
"""

import smtplib
from email.mime.text import MIMEText
from lib.other_tools.allure_data.allure_report_data import TestMetrics, AllureFileClean
from lib import config


class SendEmail:
    """发送邮箱"""
    def __init__(self, metrics: TestMetrics):
        self.metrics = metrics
        self.allure_data = AllureFileClean()
        self.CaseDetail = self.allure_data.get_failed_cases_detail()

    @classmethod
    def send_mail(cls, user_list: list, sub, content: str) -> None:
        """

        :param user_list: 发件人邮箱
        :param sub:
        :param content: 发送内容
        :return:
        """
        user = "梁灿" + "<" + config.email.send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(config.email.email_host)
        server.login(config.email.send_user, config.email.stamp_key)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def error_mail(self, error_message: str) -> None:
        """
        执行异常邮件通知
        :param error_message: 报错信息
        :return:
        """
        email = config.email.send_list
        user_list = email.split(',') # 多个邮件发送，config文件中直接添加邮件

        sub = config.project_name + "接口自动化测试执行异常通知"
        content = f"自动化测试执行完毕，程序中发生异常，请悉知。报错信息如下: \n{error_message}"
        self.send_mail(user_list, sub, content)

    def send_main(self) -> None:
        """
        发送邮件
        :return:
        """
        email = config.email.send_list
        user_list = email.split(',') #多个邮件发送，yaml文件中直接添加邮件

        sub = config.project_name + "接口自动化测试报告"
        content = f"""
        各位同事大家好！：
            自动化测试用例执行完成，执行结果如下：
            用例运行总数: {self.metrics.total}个
            通过用例个数: {self.metrics.passed}个
            失败用例个数: {self.metrics.failed}个
            异常用例个数: {self.metrics.broken}个
            跳过用例个数：{self.metrics.skipped}个
            成   功  率: {self.metrics.pass_rate} %
            
        {self.allure_data.get_failed_cases_detail()}
        
        ********************************************************
        jenkins地址: http://192.168.110.91:8081/login
        详细情况可登录jenkins平台查看，非相关负责人可忽略此消息，谢谢！
        """
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    SendEmail(AllureFileClean().get_case_count()).send_main()
