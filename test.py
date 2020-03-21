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

from xToolkit.xtime.xdatetime.xdatetime import UTC8

if __name__ == "__main__":
    # formats = ["YYYY-MM-DD", "YYYY-M-DD", "YYYY-M-D", "YYYY/MM/DD", "YYYY/M/DD", "YYYY/M/D", "YYYY.MM.DD", "YYYY.M.DD", "YYYY.M.D", "YYYYMMDD", "YYYY-DDDD",
    #            "YYYYDDDD", "YYYY-MM", "YYYY/MM", "YYYY.MM", "YYYY"]
    #
    # year = ["%y", "%Y"]
    # month = ["%m"]
    # day = ["%d"]
    # hour = ["%H"]
    # minute = ["%M"]
    # second = ["%S"]
    # microsecond = []
    # tz = []
    #
    # sign = ["-", "/"]
    #
    # a = [["%y-%m-%d %H:%M:%S"],
    #      ["%Y-%m-%d %H:%M:%S"]
    #      ]
    #
    # date_all = ["%Y-%m-%d", "%y-%m-%d"]
    # time_all = ["%H:%M:%S", "%I:%M:%S"]
    #
    # # print(datetime.now().strftime("%y-%m-%dT%H:%M:%S.%f"))
    # print(datetime.now(tz=UTC8()).isoformat())

    """
    2020-03-20T22:09:06
    2020-03-20T10:09:06.278060 PM
    2020-03-20T22:09:06.278060+08:00
    """
    time_string = "15:22:56.252525"
    print(xtime.get(time_string).format("%H:%M:%S.%f"))

