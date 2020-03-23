#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 17:27
# @Author  : 熊利宏
# @project : 直接测试模块
# @Email   : xionglihong@163.com
# @File    : test.py
# @IDE     : PyCharm
# @REMARKS : 直接测试xtoolkit库的各项模块


# time_string = [['9999-03-17 12:14:12', "%Y-%m-%d %H:%M:%S"],
#                ['12:14:12', "%H:%M:%S"],
#                ]
#
# for key in time_string:
#     print(datetime.strptime(key[0], key[1]))

import arrow

from xToolkit import VERSION, xstring, xtime

# 系统时间库
from datetime import datetime, tzinfo, timedelta

from xToolkit.xdatetime.xdatetime.xdatetime import UTC8

if __name__ == "__main__":
    print(xstring.dispose("420117198807203114").get_identity_card(True))
