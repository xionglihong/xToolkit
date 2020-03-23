#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 7:07
# @Author  : 熊利宏
# @project : 字符串处理模块
# @Email   : xionglihong@163.com
# @File    : dispose.py
# @IDE     : PyCharm
# @REMARKS : 字符串的一些常用处理

# 字符串公共功能
from ..xstring import BasicsFunction


# 字符串处理
class Dispose(object):
    """
    字符串的一些常用处理
    """

    def __init__(self, mark):
        self.__mark = mark

    # 获取身份证信息
    def get_identity_card(self, *args):
        """
        提供中国大陆身份证验证，暂时只支持效验18位身份证

        mold表示消息类型，为选填
            为空表示不输出错误或正确消息，只输出 True 或者 False，表示格式正确或者错误
            True 输出正确消息，包括出生年月，性别基础信息
            False 输出完整身份证信息，包括市县，出生年月日，性别等信息，但速度比较慢，因为是进行的网络查询
        """
        return BasicsFunction(self.__mark).identity_card(args[0])
