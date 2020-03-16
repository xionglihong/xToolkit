#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 23:28
# @Author  : 熊利宏
# @project : 普通测试
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


if __name__ == "__main__":
    test_xt = TestXToolkit()

    a = test_xt.get_timestamp_int(test_data["_int"])
    b = arrow.get(test_data["_int"])

    print(a)
    print(b)
    print(type(a))
    print(type(b))
