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
import time

# 第三方时间模块
from dateutil.relativedelta import relativedelta  # 时间推移
from dateutil.parser import parse  # 时间字符串解析


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

    # 时间字符串效验->(true,false)
    @staticmethod
    def datetime_string_true(string):

        try:
            parse(string)
            return True
        except ValueError:
            return False

    # 时间转时间戳
    @staticmethod
    def datetime_to_timestamp(times):
        return time.mktime(times.timetuple())


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

    # 时间戳转时间
    @classmethod
    def timestamp_to_space(cls, timestamp, tz=None):
        dt = datetime.fromtimestamp(timestamp, tz=UTC8() if not tz else tz)
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    # 时间字符串转时间
    @classmethod
    def string_to_space(cls, string):
        """
        时间字符串解析
        """
        try:
            # 利用parse进行时间字符串解析
            dt = parse(string)
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)
        except ValueError:
            raise ValueError("时间字符串解析错误,解析错误的字符串为 {}".format(string))

    # datetime转时间
    @classmethod
    def datetime_to_space(cls, dt):
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    # date转时间
    @classmethod
    def date_to_space(cls, dt):
        return cls(dt.year, dt.month, dt.day)

    # 时间格式化输出
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
            %f  微秒
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

    # 输出 datetime 类型
    def former_type(self):
        """
        输出datetime数据类型
        """
        return self._datetime

    # 时间戳
    @property
    def timestamp(self):
        """
        datetime 对象转时间戳
        输出没有毫秒部分，如果要毫秒部分就用time.time()
        """
        return time.mktime(self._datetime.timetuple())

    # 年
    @property
    def year(self):
        return self._datetime.year

    # 月
    @property
    def month(self):
        return self._datetime.month

    # 日
    @property
    def day(self):
        return self._datetime.day

    # 时
    @property
    def hour(self):
        return self._datetime.hour

    # 分
    @property
    def minute(self):
        return self._datetime.minute

    # 秒
    @property
    def second(self):
        return self._datetime.second

    # 微妙
    @property
    def microsecond(self):
        return self._datetime.microsecond

    # 时间推移
    def shift(self, **kwargs):
        """
        参数:
        years 年
        months 月
        days 日
        weeks 周
        hours 时
        minutes 分
        seconds 秒
        microseconds 微妙
        """
        dt = self._datetime + relativedelta(**kwargs)
        return self.datetime_to_space(dt)

    # 时间替换
    def replace(self, **kwargs):
        """
        参数:
            year 年
            month 月
            day 日
            hour 时
            minute 分
            second 秒
            microsecond 微妙
        """
        dt = self._datetime.replace(**kwargs)
        return self.datetime_to_space(dt)


# 时间高级类
class Compare(object):
    """
    时间高级类
    """

    def __init__(self, *args, **kwargs):
        self.arg = args
        self.kwarg = kwargs

    # 比较二个时间的差值，返回秒值
    @property
    def how(self):
        start = parse(self.arg[0])  # 开始时间
        end = parse(self.arg[1])  # 结束时间

        how = BasicFunction.datetime_to_timestamp(start) - BasicFunction.datetime_to_timestamp(end)
        return int(how)

    # 返回指定月份的最后一天
    @property
    def last(self):
        year = self.arg[0]  # 年
        month = self.arg[1]  # 月

        # 获取要计算的时间，先得到下个月的第一天，再减去一天
        space = Space(year, month, 1).shift(months=1).shift(days=-1).format("%Y-%m-%d")

        return space
