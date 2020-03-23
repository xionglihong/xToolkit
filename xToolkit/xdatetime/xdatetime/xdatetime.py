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
from datetime import datetime, tzinfo, timedelta


# 自定义时区
class UTC8(tzinfo):
    """
    自定义时区，默认为UTC +8:00，也就是北京时间
    hours->[-23,24] minutes->[-59,59]
    注意：时间和分钟正负保持一致
    """

    def __init__(self, hours=8, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def utcoffset(self, dt):
        return timedelta(hours=self.hours, minutes=self.minutes)

    def tzname(self, dt):
        return "UTC({:+}:{:0>2d})".format(self.hours, self.minutes)

    def dst(self, dt):
        return timedelta(hours=self.hours, minutes=self.minutes)


# 时间基础功能
class BasicFunction(object):
    """
    时间模块的一些基础功能
    """

    # 时间字符串效验
    @staticmethod
    def __datetime_string(string):

        # 时间字符串解析模板
        matching = ""

        # 记录是否存在日期部分
        is_have_date = 0

        # 日期部分
        if "-" in string:
            matching += "%Y-%m-%d"

            is_have_date = 1
        elif "/" in string:
            matching += "%Y/%m/%d"

            is_have_date = 1
        elif string.count(".") == 2 or string.count(".") == 3:
            matching += "%Y.%m.%d"

            is_have_date = 1

        # 时间部分
        if ":" in string:
            if "T" in string:
                matching += "T%H:%M:%S"
            else:
                if is_have_date:
                    matching += " %H:%M:%S"
                else:
                    matching += "%H:%M:%S"
        # 微妙部分
        if string.count(".") == 3 or string.count(".") == 1:
            matching += ".%f"

        # 时区部分
        if "+" in string or string.count("-") == 3:
            matching += "%z"

        return matching

    # 时间字符串效验->(true,false)
    def datetime_string_true(self, string):
        matching = self.__datetime_string(string)

        try:
            datetime.strptime(string, matching)
            return True
        except ValueError:
            return False

    # 时间字符串效验->字符串解析模板
    def datetime_string_template(self, string):
        return self.__datetime_string(string)


# 基础功能
class Space(object):
    """
    实现时间模块的基础功能

    参数：
        year：年
        month：月
        day：日
        hour：(可选)时间。默认值为0。
        minute：(可选)分钟，默认为0。
        second：(可选)秒，默认为0。
        microsecond：(可选)微秒。默认值0。
        tz：时区
    """

    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0, tz=None):
        self._datetime = datetime(year, month, day, hour, minute, second, microsecond, tz)

    def __str__(self):
        return self._datetime.isoformat()

    # 当前时间
    @classmethod
    def now(cls, tz=UTC8()):
        dt = datetime.now(tz=tz)
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    # 时间格式化
    def format(self, *args):
        """
        默认格式："%Y-%m-%d %H:%M:%S"

        常用格式：
            "%Y-%m-%dT%H:%M:%S.%f%z"


        输出参数：
            %y	两位数的年份表示（00-99）
            %Y	四位数的年份表示（000-9999）
            %m	月份（01-12）
            %d	月内中的一天（0-31）
            %H	24小时制小时数（0-23）
            %I	12小时制小时数（01-12）
            %M	分钟数（00=59）
            %S	秒（00-59）
            %f  毫秒
            %a	本地简化星期名称
            %A	本地完整星期名称
            %b	本地简化的月份名称
            %B	本地完整的月份名称
            %c	本地相应的日期表示和时间表示
            %j	年内的一天（001-366）
            %p	本地A.M.或P.M.的等价符
            %U	一年中的星期数（00-53）星期天为星期的开始
            %w	星期（0-6），星期天为星期的开始
            %W	一年中的星期数（00-53）星期一为星期的开始
            %x	本地相应的日期表示
            %X	本地相应的时间表示
            %Z	当前时区的名称
            %%	%号本身
        """
        arg = len(args)

        style = "%Y-%m-%d %H:%M:%S"
        # 根据args长度，设置输出格式style
        if arg == 0:
            style = "%Y-%m-%d %H:%M:%S"
        elif arg == 1:
            style = args[0]
        elif arg >= 2:
            raise ValueError("暂时只接受一个参数")

        return self._datetime.strftime(style)

    # 时间戳转时间
    @classmethod
    def timestamp_to_time(cls, timestamp, tz=None):
        dt = datetime.fromtimestamp(timestamp, tz=UTC8() if not tz else tz)
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    # 字符串转时间
    @classmethod
    def string_to_time(cls, string, formatting=None):
        """
        formatting不为空时，利用传入格式解析时间字符串，若为空则尝试从模板库解析时间字符串
        """

        if formatting:
            matching = formatting
        else:
            # 时间模块基础功能
            basic = BasicFunction()

            # 时间字符串解析模块
            matching = basic.datetime_string_template(string)

        try:
            dt = datetime.strptime(string, matching)
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)
        except ValueError:
            raise ValueError("解析时间字符串错误,解析表达式为: {} 时间字符串为: {}".format(matching, string))
