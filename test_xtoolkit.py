#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 23:28
# @Author  : 熊利宏
# @project : 自动测试
# @Email   : xionglihong@163.com
# @File    : test.py
# @IDE     : PyCharm

from xToolkit import xdatetime

# 第三方库
import arrow

# 全局变量，用于测试数据
test_data = {
    "_int": 1584321366,  # int时间戳 1584321366 北京时间 2020-03-16 09:16:06
}


# 功能模块
class TestXToolkit(object):
    """
    编写所有需要测试的功能模块
    """

    # 版本号
    @staticmethod
    def version():
        return xdatetime.version()

    # get方法-->时间戳-->int
    @staticmethod
    def get_timestamp_int(timestamp):
        return xdatetime.get(timestamp)


test_xt = TestXToolkit()


# 版本号
def test_version():
    from xToolkit.api import VERSION
    assert test_xt.version() == VERSION


# get方法-->时间戳-->int
def test_get_timestamp_int():
    timestamp = test_data["_int"]
    # 此处要进行输出格式化，不然会出现，输出样式一样，但是结果不一样，因为基类不一样
    assert test_xt.get_timestamp_int(timestamp) == arrow.get(timestamp)
