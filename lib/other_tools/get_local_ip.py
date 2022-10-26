#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022/10/26 12:17
# @Author : 梁灿
# @Email : 1473166229@qq.com
# @File :
# @decribe:

import socket


def get_host_ip():
    """
    查询本机IP地址
    :return:
    """
    _s = None
    try:
        _s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        _s.connect(('8.8.8.8',80))
        l_host = _s.getsockname()[0]
    finally:
        _s.close()

    return l_host

