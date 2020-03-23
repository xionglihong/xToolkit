#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 20:39
# @Author  : 熊利宏
# @project : 基类模块
# @Email   : xionglihong@163.com
# @File    : judgement.py
# @IDE     : PyCharm
# @REMARKS : 进行格式判断

# 时间模块
from ..xdatetime.xdatetime.xdatetime import BasicFunction


# 类型判断
class JudgeType(object):
    """
    判断输入的值得类型
    """

    # 整形或者浮点型
    @staticmethod
    def is_timestamp(value):
        """
        检查值是否为浮点型或者整形，同时可以判断值是否为时间戳，时间戳就是浮点数或者整数
        """
        if isinstance(value, bool):
            return False
        if not (isinstance(value, int) or isinstance(value, float) or isinstance(value, str)):
            return False

        try:
            float(value)
            return True
        except ValueError:
            return False

    # 字符串类型
    @staticmethod
    def is_string(value):
        return isinstance(value, str)

    # 时间字符串
    @staticmethod
    def is_datetime_string(value):
        # 时间模块基础功能
        basic = BasicFunction()

        # 判断是否为时间戳
        if not JudgeType.is_timestamp(value):
            return False

        # 判断是否为时间字符串
        if not basic.datetime_string_true(value):
            return False

        return True
