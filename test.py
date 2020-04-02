#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 17:27
# @Author  : 熊利宏
# @project : 直接测试模块
# @Email   : xionglihong@163.com
# @File    : test.py
# @IDE     : PyCharm
# @REMARKS : 直接测试xtoolkit库的各项模块

import arrow

from datetime import datetime, date
import time

from xToolkit.xdatetime.xdatetime.xdatetime import UTC8

from xToolkit import xstring, xdatetime

if __name__ == "__main__":
    print(xdatetime.get().timestamp)
    print(xdatetime.get("2020-04-02 21:26:54").timestamp)

    print(xdatetime.get().year)
    print(xdatetime.get().month)
    print(xdatetime.get().day)
    print(xdatetime.get().hour)
    print(xdatetime.get().minute)
    print(xdatetime.get().second)
    print(xdatetime.get().microsecond)






