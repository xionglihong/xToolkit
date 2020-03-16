#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 22:22
# @Author  : 熊利宏
# @project : 时间模块
# @Email   : xionglihong@163.com
# @File    : api.py
# @IDE     : PyCharm

from .xdatetime import XDateReady

# 实例化时间模块
xdt = XDateReady()


# 版本号
def version():
    """
    输出版本号
    """
    return xdt.version()


# get方法
def get(*args, **kwargs):
    """
    实现，时间格式判断，获取当前时间，时间推移，时间间隔等功能
    """
    return xdt.get(*args, **kwargs)
