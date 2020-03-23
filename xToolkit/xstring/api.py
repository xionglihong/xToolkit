#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 20:52
# @Author  : 熊利宏
# @project : 字符串模块
# @Email   : xionglihong@163.com
# @File    : api.py
# @IDE     : PyCharm
# @REMARKS : 字符串模块的对外接口

# 总基类
from ..xtoolkit import XToolkit

# 字符串验证模块
from .check.check import CheckData

# 字符串处理模块
from .dispose.dispose import Dispose


# 字符串基类
class XString(XToolkit):

    def __init__(self, checks=CheckData, dispose=Dispose):
        # 继承父类的init方法
        super(XString, self).__init__()
        # self.judge->类型判断

        # 效验模块
        self.__checks = checks

        # 基础处理
        self.__disposes = dispose

    # 格式效验
    def check(self, *args):
        """
        格式验证，args第一个参数为要验证的字符串
        """
        if len(args) == 1:
            mark = args[0]
            return self.__checks(mark)
        else:
            raise ValueError("check() 方法暂时只支持一个参数并且不能为空")

    # 基础处理
    def dispose(self, *args):
        """
        基础处理，args第一个参数为要处理的字符串
        """
        if len(args) == 1:
            mark = args[0]
            return self.__disposes(mark)
        else:
            raise ValueError("check() 方法暂时只支持一个参数并且不能为空")
