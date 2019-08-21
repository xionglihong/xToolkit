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


# 身份证效验
def identity(strings):
    """
    输入身份证号码，进行效验，如果合规，返回 code 为0000，如果不合规返回其他编号，并提示不合格原因
    如果合规返回，成功表示Turn表示，生日，归属地
    """
    return DataProofreading().identity(strings)


# 手机号码效验
def cellphone(strings):
    """
    移动：134、135、136、137、138、139、150、151、152、157(TD)、158、159、178(新)、182、184、187、188
    联通：130、131、132、152、155、156、185、186
    电信：133、153、170、173、177、180、181、189、（1349卫通）
    总结起来就是第一位必定为1，第二位必定为3或5或8，其他位置的可以为0 - 9
    使用正则表达式 ^1[3|5|7|8|][0-9]{9}$
    """
    return DataProofreading().cellphone(strings)


# 效验数字
def figure(strings, mold=1):
    """
    Python 中已经有效验整数的方法 isdigit，只能效验整数
    此方法新增其他的一些数字效验
    mole的值为：
    1.代表 正浮点型或者正整形
    """
    return DataProofreading().figure(strings, mold)
