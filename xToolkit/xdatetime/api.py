#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 22:22
# @Author  : 熊利宏
# @project : 时间模块
# @Email   : xionglihong@163.com
# @File    : api.py
# @IDE     : PyCharm
# @REMARKS : 时间模块的对外接口

# 总基类
from ..xtoolkit import XToolkit

# 时间模块基础功能
from .xdatetime.xdatetime import Space, Compare

# 系统时间库
from datetime import datetime, date

# 时区
from .xdatetime.xdatetime import UTC8


# 时间模块基类
class XDateTime(XToolkit):

    def __init__(self):
        # 继承父类的init方法
        super(XDateTime, self).__init__()
        # self.judge->类型判断

        # 指向时间基类
        self.limit = Space

        # 指向时间比较类
        self.compare = Compare

    # get 方法
    def get(self, *args, **kwargs):

        """
        可接受值类型：不传值，时间戳
        输出时间格式默认为ISO 8601标准化日期，年-月-日 时:分：秒.微妙 时区

        args：
            空值：输出本地当前时间,默认北京时间UTC+8

        kwargs：
            tz：表示时区
        """
        args_count = len(args)

        # kwargs里面的参数tz为时区，不传代表输出北京时间UTC(+8:00)
        if args_count == 0:
            tz = kwargs.get("tz", None)
            if tz:
                return self.limit.now(tz=tz)
            else:
                return self.limit.now()

        # 若参数为一个，整体返回UTC时间
        elif args_count == 1:
            arg = args[0]

            # 时间戳(int,float)
            if not self.judge.is_string(arg) and self.judge.is_timestamp(arg):
                # 时区的默认值为 None
                return self.limit.timestamp_to_space(arg, tz=kwargs.get("tz", None))

            # 字符串
            elif self.judge.is_string(arg):
                # 时间字符串若满足时间戳，直接进行时间戳转时间处理
                if self.judge.is_timestamp(arg):
                    arg = self.judge.to_digital(arg)

                    return self.limit.timestamp_to_space(arg, tz=kwargs.get("tz", None))
                # 若不为时间戳格式，进行时间字符串解析
                else:
                    # 时间字符串解析
                    return self.limit.string_to_space(arg)

            # datetime
            elif isinstance(arg, datetime):
                return self.limit.datetime_to_space(arg)

            # date
            elif isinstance(arg, date):
                return self.limit.date_to_space(arg)

        # 参数为二个
        elif args_count == 2:
            start, end = args[0], args[1]

            return self.compare(start, end)

    # shape 方法
    def shape(self, *args, **kwargs):
        """
        判断字符串是否为时间字符串
        """
        if len(args) == 0:
            raise ValueError("需要验证的字符串不能为空")
        else:
            arg = args[0]
            return self.judge.is_datetime_string(arg)

    # 时区
    @staticmethod
    def utc8(*args, **kwargs):
        return UTC8(hours=kwargs.get("hours", 8), minutes=kwargs.get("minutes", 0))
