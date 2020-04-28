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
from dateutil.parser import parse  # 时间字符串解析

from datetime import datetime, date
import time

from xToolkit.xdatetime.xdatetime.xdatetime import UTC8

from xToolkit import xstring, xdatetime

if __name__ == "__main__":
    # a = xdatetime.get("2020-04-28 10:52:52", "1988-07-20 17:31:12").how
    # print(a)
    print(925271696-1588046221)
