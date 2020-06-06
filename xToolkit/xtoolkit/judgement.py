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

    # 整形
    @staticmethod
    def is_int(value):
        """
        判断输入的是否为整数，包括数组整数和字符串整数
        补充了系统的isdigit功能
        """
        try:
            int(value)

            # 排除掉浮点数
            if "." in str(value):
                return False

            return True
        except (TypeError, ValueError):
            return False

    # 字符串类型
    @staticmethod
    def is_string(value):
        return isinstance(value, str)

    # 时间字符串
    @staticmethod
    def is_datetime_string(value):
        """
        判断是否为时间字符串，包括类型 时间戳，时间字符串，xdatetime
        """
        # 时间模块基础功能
        basic = BasicFunction()

        if JudgeType.is_timestamp(value) or basic.datetime_string_true(value):
            return True
        else:
            return False

    # 转换为整形或者浮点型
    @staticmethod
    def is_digital(value):
        """
        判断传入是否为数字，包括整形或者浮点型
        """
        return JudgeType.is_timestamp(value)

    # 转换为整形或者浮点型
    @staticmethod
    def to_digital(value):
        """
        传入的值必须为浮点型或者整形字符串或者数字，若为浮点型返回浮点型，若为整形返回整形
        """
        value = str(value)

        # 判断是否为浮点型或者整形
        if not JudgeType.is_digital(value):
            raise ValueError("传入的值必须为浮点型或者整形字符串或者数字")

        if "." in value:
            result = float(value)
        else:
            result = int(value)

        return result
