#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 17:27
# @Author  : 熊利宏
# @project : 直接测试模块
# @Email   : xionglihong@163.com
# @File    : test.py
# @IDE     : PyCharm
# @REMARKS : 直接测试xtoolkit库的各项模块

from datetime import datetime, date

from xToolkit.xdatetime.xdatetime.xdatetime import UTC8

from xToolkit import xstring, xdatetime

if __name__ == "__main__":
    a1 = xdatetime.shape("2020-03-20 22:09:06")
    print(a1)
