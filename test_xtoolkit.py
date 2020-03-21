#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 23:28
# @Author  : 熊利宏
# @project : 自动测试
# @Email   : xionglihong@163.com
# @File    : test.py
# @IDE     : PyCharm

import pytest

from xToolkit import xstring, xtime

# 自定义时区
from xToolkit.xtime.xdatetime.xdatetime import UTC8

import arrow


# 字符串模块
class TestXstring(object):

    # 判断check不传值
    def test_check_no(self):
        with pytest.raises(ValueError) as example:
            xstring.check().is_identity_card()
        assert str(example.value) == "check() 方法暂时只支持一个参数并且不能为空"

    # 验证 ——> 车牌号
    car_number = [("鄂A96288", True), ("鄂BF12345", True), ("鄂A962889", False), ("鄂BF123456", False), ("川A123AB", True), ("川A2222学", True),
                  ("川A12345D", True), ("川A123456", False), ("川A2222i", False), ("川AA12345", False), ("川AD123456", False), ("川AF12345", True)]

    @pytest.mark.parametrize("car,result", car_number)
    def test_car_number(self, car, result):
        assert xstring.check(car).is_car_number() == result

    # 验证 ——> 身份证
    identity_card = [("421122199407295810", True), ("422421196711236820", True), ("42098419911025661X", True),
                     ("420123197010226928", True), ("422121197211130454", True), ("532626198909181746", True),
                     ("42100219891115244", False), ("4211221982042796340", False), ("920124198110152322", False),
                     ("421122199407295870", False), ("422421496711236820", False), ("40098419911025661X", False)]

    @pytest.mark.parametrize("identity,result", identity_card)
    def test_identity_card(self, identity, result):
        assert xstring.check(identity).is_identity_card() == result

    # 验证 ——> 身份证（输出错误结果）
    identity_card_true = [("42100219891115244", {'code': '0001', 'msg': '待验证的值长度必须为18位', 'data': None}),
                          ("4211221982042796340", {'code': '0001', 'msg': '待验证的值长度必须为18位', 'data': None}),
                          ("920124198110152322", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None}),
                          ("421122199407295870", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None}),
                          ("422421496711236820", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None}),
                          ("40098419911025661X", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None})]

    @pytest.mark.parametrize("identity,result", identity_card_true)
    def test_identity_card_true(self, identity, result):
        assert xstring.check(identity).is_identity_card(True) == result


# 时间模块
class TestXtime(object):

    # 获取本地时间
    def test_get_now(self):
        assert xtime.get().format() == arrow.now().format("YYYY-MM-DD HH:mm:ss")

    # 获取UTC时间
    def test_get_utc_now(self):
        assert xtime.get(tz=UTC8(hours=0, minutes=0)).format() == arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")

    timestamp_data = [1584689499.2525, 1584689499, 1584689499.252555, 1584689499.12457899999, 1584]

    # 时间戳转时间格式(UTC)
    @pytest.mark.parametrize("timestamp", timestamp_data)
    def test_timestamp_utc_datetime(self, timestamp):
        assert xtime.get(timestamp, tz=UTC8(hours=0, minutes=0)).format() == arrow.get(timestamp).format("YYYY-MM-DD HH:mm:ss")

    # 时间戳转时间格式(北京时间)
    @pytest.mark.parametrize("timestamp", timestamp_data)
    def test_timestamp_beijing_datetime(self, timestamp):
        assert xtime.get(timestamp).format() == arrow.get(timestamp, tzinfo=UTC8()).format("YYYY-MM-DD HH:mm:ss")

    all_datetime_string = [
        # 完整日期，时间，微秒，时区
        ("2020-03-20T22:09:06.252525+0800", "%Y-%m-%dT%H:%M:%S.%f%z"),
        ("2020-03-20 10:09:06.252525+0800", "%Y-%m-%d %H:%M:%S.%f%z"),
        ("2020/03/20T10:09:06.252525+0800", "%Y/%m/%dT%H:%M:%S.%f%z"),

        # 日期时间
        ("2020-03-20T22:09:06", "%Y-%m-%dT%H:%M:%S"),
        ("2020-03-20 10:09:06", "%Y-%m-%d %H:%M:%S"),
        ("2020/03/20 10:09:06", "%Y/%m/%d %H:%M:%S"),
        ("2020.03.20 10:09:06", "%Y.%m.%d %H:%M:%S"),

        # 秒级时间
        ("15:22:56", "%H:%M:%S"),

        # 微秒级时间
        ("15:22:56.252525", "%H:%M:%S.%f"),
    ]

    # 时间字符串转时间（完整日期，时间，微秒，时区）
    @pytest.mark.parametrize("all_datetime_string,formatting", all_datetime_string)
    def test_string_to_microsecond(self, all_datetime_string, formatting):
        assert xtime.get(all_datetime_string).format(formatting) == all_datetime_string
