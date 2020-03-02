#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 11:36
# @Author  : 熊利宏
# @project : 项目名称
# @Email   : xionglihong@163.com
# @File    : collect.py
# @IDE     : PyCharm

# 正则表达式校对
from xToolkit.xstring.verification import DataProofreading


# 数据效验
def verified(strings, dtype="float_int"):
    """
    dtype 的值为：
    identity：进行中国大陆身份证效验
    iphone：手机号码效验
    float_int：浮点型或者整形(正负都可以)
    float：浮点型(正负都可以)
    name：姓名（只含中文）
    bank：银行卡效验
    """
    return DataProofreading().verified(strings=strings, dtype=dtype)
