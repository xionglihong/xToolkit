#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 16:07
# @Author  : 熊利宏
# @project : 工具集总基类
# @Email   : xionglihong@163.com
# @File    : xtoolkit.py
# @IDE     : PyCharm

# 格式判断
from .judgement import JudgeType


# 总基类
class XToolkit(object):
    """
    工具集的总基类
    """

    def __init__(self):
        # 格式判断
        self.judge = JudgeType()
