#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 16:25
# @Author  : 熊利宏
# @project : 时间模块
# @Email   : xionglihong@163.com
# @File    : xdatetime.py
# @IDE     : PyCharm

from __future__ import absolute_import

# 系统时间库
from datetime import datetime
from datetime import tzinfo as dt_tzinfo

# 时间库
from dateutil import tz as dateutil_tz

# 正则表达式
import re

# 总基类
# 此处不能进行相对导入，二个顶级包不能进行相对导入
from xToolkit.xtoolkit import XToolkit

# 版本号
from ..api import VERSION


# 基础功能
class BasicFunction(object):
    """
    基础功能
    """

    # 解析时区表达式
    @classmethod
    def parse(cls, tzinfo_string):

        _TZINFO_RE = re.compile(r"^([\+\-])?(\d{2})(?:\:?(\d{2}))?$")

        tzinfo = None

        if tzinfo_string == "local":
            tzinfo = dateutil_tz.tzlocal()

        elif tzinfo_string in ["utc", "UTC", "Z"]:
            tzinfo = dateutil_tz.tzutc()

        else:

            iso_match = _TZINFO_RE.match(tzinfo_string)

            if iso_match:
                sign, hours, minutes = iso_match.groups()
                if minutes is None:
                    minutes = 0
                seconds = int(hours) * 3600 + int(minutes) * 60

                if sign == "-":
                    seconds *= -1

                tzinfo = dateutil_tz.tzoffset(None, seconds)

            else:
                tzinfo = dateutil_tz.gettz(tzinfo_string)

        if tzinfo is None:
            raise ValueError('无法解析时区表达式 "{}"'.format(tzinfo_string))

        return tzinfo

    # 判断数据类型
    @classmethod
    def is_str(cls, string):
        """
        判断传入值是否为字符串类型
        """
        return isinstance(string, str)

    # 判断是否为时间戳
    @classmethod
    def is_timestamp(cls, value):
        """
        判断传入值是否为时间戳格式
        """
        if isinstance(value, bool):
            return False
        if not isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
            return False
        try:
            float(value)
            return True
        except ValueError:
            return False


# 时间基类
class XDataTime(XToolkit):
    """
    1.时间模块基类
    2.以系统时间库datetime为基础，并在此基础上扩充了部分功能

    参数：
        year：年
        month：月
        day：日
        hour：(可选)时间。默认值为0。
        minute：(可选)分钟，默认为0。
        second：(可选)秒，默认为0。
        microsecond：(可选)微秒。默认值0。
        tzinfo：时区，默认为UTC，协调世界时
    """
    # 实例化基础功能类
    basic = BasicFunction()

    resolution = datetime.resolution

    _ATTRS = ["year", "month", "day", "hour", "minute", "second", "microsecond"]
    _ATTRS_PLURAL = ["{}s".format(a) for a in _ATTRS]
    _MONTHS_PER_QUARTER = 3
    _SECS_PER_MINUTE = float(60)
    _SECS_PER_HOUR = float(60 * 60)
    _SECS_PER_DAY = float(60 * 60 * 24)
    _SECS_PER_WEEK = float(60 * 60 * 24 * 7)
    _SECS_PER_MONTH = float(60 * 60 * 24 * 30.5)
    _SECS_PER_YEAR = float(60 * 60 * 24 * 365.25)

    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):

        # 判断时区
        if tzinfo is None:
            tzinfo = dateutil_tz.tzutc()
        elif isinstance(tzinfo, dt_tzinfo) and hasattr(tzinfo, "localize") and hasattr(tzinfo, "zone") and tzinfo.zone:
            tzinfo = XDataTime.basic.parse(tzinfo.zone)
        elif XDataTime.basic.is_str(tzinfo):
            tzinfo = XDataTime.basic.parse(tzinfo)

        self._datetime = datetime(year, month, day, hour, minute, second, microsecond, tzinfo)

    def __str__(self):
        return self._datetime.isoformat()

    # 版本号
    @staticmethod
    def version():
        return VERSION

    # 获取本机时间
    @classmethod
    def now(cls, tzinfo=None):
        if tzinfo is None:
            tzinfo = dateutil_tz.tzlocal()
        dt = datetime.now(tzinfo)

        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    # 获取调协时间
    @classmethod
    def utc_now(cls):
        dt = datetime.now(dateutil_tz.tzutc())

        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    # 格式化时间戳
    @classmethod
    def fromtimestamp(cls, timestamp, tzinfo=None):
        """
        格式化时间戳

        参数：
            timestamp：时间戳
            tzinfo：时区,默认为本地时间
        """

        if tzinfo is None:
            tzinfo = dateutil_tz.tzlocal()
        elif cls.basic.is_str(tzinfo):
            tzinfo = cls.basic.parse(tzinfo)

        if not cls.basic.is_timestamp(timestamp):
            raise ValueError("提供的时间戳'{}'格式错误.".format(timestamp))

        dt = datetime.fromtimestamp(float(timestamp), tzinfo)

        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)


# 时间预处理
class XDateReady(object):

    def __init__(self):
        self.limit = XDataTime

        # 实例化基础功能类
        self.basic = BasicFunction()

    # 预处理
    def get(self, *args, **kwargs):
        """
        可接受值类型：XDateTime(本模块定义类型)，datetime(python内置日期时间类型),string，空置，None
        """
        args_count = len(args)
        tz = kwargs.get("tzinfo", None)

        # 参数若为零个，输出本地时间
        if args_count == 0:
            return self.limit.now()

        # 若参数为一个
        elif args_count == 1:
            arg = args[0]

            # 参数为None时，返回调协时间
            if arg is None:
                return self.limit.utc_now()

            # 参数为（整形，浮点型）
            elif not self.basic.is_str(arg) and self.basic.is_timestamp(arg):
                if tz is None:
                    # 默认设置为UTC
                    tz = dateutil_tz.tzutc()
                return self.limit.fromtimestamp(arg, tzinfo=tz)
