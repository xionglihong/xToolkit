#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 23:28
# @Author  : 熊利宏
# @project : 自动测试
# @Email   : xionglihong@163.com
# @File    : test.py
# @IDE     : PyCharm

import pytest

from xToolkit import xstring, xdatetime

# 自定义时区
from xToolkit.xdatetime.xdatetime.xdatetime import UTC8

from datetime import datetime, date
import arrow


# 字符串验证模块（check）
class TestXstringCheck(object):

    # 判断check不传值
    def test_check_no(self):
        with pytest.raises(ValueError) as example:
            xstring.check().is_identity_card()
        assert str(example.value) == "check() 方法暂时只支持一个参数并且不能为空"

    # 车牌号
    car_number = [("鄂A96288", True), ("鄂BF12345", True), ("鄂A962889", False), ("鄂BF123456", False), ("川A123AB", True), ("川A2222学", True),
                  ("川A12345D", True), ("川A123456", False), ("川A2222i", False), ("川AA12345", False), ("川AD123456", False), ("川AF12345", True)]

    @pytest.mark.parametrize("car,result", car_number)
    def test_car_number(self, car, result):
        assert xstring.check(car).is_car_number == result

    # 身份证
    identity_card = [("421122199407295810", True), ("422421196711236820", True), ("42098419911025661X", True),
                     ("420123197010226928", True), ("422121197211130454", True), ("532626198909181746", True),
                     ("42100219891115244", False), ("4211221982042796340", False), ("920124198110152322", False),
                     ("421122199407295870", False), ("422421496711236820", False), ("40098419911025661X", False)]

    @pytest.mark.parametrize("identity,result", identity_card)
    def test_identity_card(self, identity, result):
        assert xstring.check(identity).is_identity_card == result

    # 时间字符串
    datetime_string = [("2020-03-23 00:00:00", True), (25251425, True), (253698.25, True), ("2020-03-", False), ("english", False), ("我是一个兵", False),
                       ("258741", True), ("2020/03/20T10:09:06.252525+0800", True)]

    @pytest.mark.parametrize("times,result", datetime_string)
    def test_datetime_string(self, times, result):
        assert xstring.check(times).is_datetime_string == result

    # 整形或浮点型
    float_or_int = [(1212, True), (25251425, True), (253698.25, True), (0.455, True), ("english", False), ("我是一个兵", False),
                    ("258741", True), (".325", True)]

    @pytest.mark.parametrize("ints,result", float_or_int)
    def test_int_or_float(self, ints, result):
        assert xstring.check(ints).is_int_or_float == result

    # URL地址
    url_data = [("https://www.baidu.com", True), ("ftp://www.baidu.com", True), ("https://www.baidu", True), ("https://192.168.0.125", True),
                ("abc", False), ("19583", False), ("你好", False), ("www.baidu.com", False)]

    @pytest.mark.parametrize("urls,result", url_data)
    def test_is_url(self, urls, result):
        assert xstring.check(urls).is_url == result

    # 手机号
    phone_data = [("15172383635", True), ("15172383635k", False), ("1517238363*", False), ("05172383635", False), ("1517283635", False), ("95172383635", False)]

    @pytest.mark.parametrize("phones,result", phone_data)
    def test_is_phone(self, phones, result):
        """
        第一位为1，一共11位数字几个
        """
        assert xstring.check(phones).is_phone == result

    # 银行卡
    bank_data = [("6222600260001072444", True), ("0222600260001072444", False), ("9222600260001072444", True), ("62226072444", False), ("622260026000107244499999999", False)]

    @pytest.mark.parametrize("banks,result", bank_data)
    def test_is_bank_number(self, banks, result):
        """
        第一位不能为0,并且13到19位数字
        """
        assert xstring.check(banks).is_bank_number == result

    # 用户姓名
    name_data = [("熊利宏", True), ("665", False), ("", False), ("熊利宏订单", False), ("熊利宏d", False)]

    @pytest.mark.parametrize("names,result", name_data)
    def test_is_user_name(self, names, result):
        """
        姓名要求为2-4个中文
        """
        assert xstring.check(names).is_user_name == result

    # 密码
    password_data = [("liehuoER880725", True), ("lieh", False), ("878787", False), ("lj5", False), ("fff999999999999999999999999999999999999999", False)]

    @pytest.mark.parametrize("passwords,result", password_data)
    def test_is_user_password(self, passwords, result):
        """
        包含6-18位字符，必须包含字母与数字，可以包含特殊字符
        """
        assert xstring.check(passwords).is_user_password == result

    # 邮箱
    mailbox_data = [("xionglihong@163.com", True), ("很好的@163.com", True), ("xionglihong163.com", False), ("xionglihong@163", False), ("123466799@163", False)]

    @pytest.mark.parametrize("mailbox,result", mailbox_data)
    def test_is_mailbox(self, mailbox, result):
        """
        第一种：只允许英文字母、数字、下划线、英文句号、以及中划线组成
        第二种：名称允许汉字、字母、数字，域名只允许英文域名
        二种中任何一种即可
        :return:
        """
        assert xstring.check(mailbox).is_mailbox == result


# 字符串处理模块
class TestXstringDispose(object):
    # 验证 ——> 身份证（输出结果）
    identity_card_true = [("42100219891115244", {'code': '0001', 'msg': '待验证的值长度必须为18位', 'data': None}),
                          ("4211221982042796340", {'code': '0001', 'msg': '待验证的值长度必须为18位', 'data': None}),
                          ("920124198110152322", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None}),
                          ("421122199407295870", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None}),
                          ("422421496711236820", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None}),
                          ("420117198807203114", {'code': '0000', 'data': {'birthday': '1988-07-20', 'gender': '男'}, 'msg': '身份证格式正确'}),
                          ("40098419911025661X", {'code': '0001', 'msg': '效验码综合验证失败', 'data': None})]

    @pytest.mark.parametrize("identity,result", identity_card_true)
    def test_identity_card_get(self, identity, result):
        assert xstring.dispose(identity).get_identity_card(True) == result


# 时间模块get方法
class TestXDateTimeGet(object):

    # 获取本地时间
    def test_get_now(self):
        assert xdatetime.get().format() == arrow.now().format("YYYY-MM-DD HH:mm:ss")

    # 获取UTC时间
    def test_get_utc_now(self):
        assert xdatetime.get(tz=UTC8(hours=0, minutes=0)).format() == arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")

    timestamp_data = [1584689499.2525, 1584689499, 1584689499.252555, 1584689499.12457899999, 1584]

    # 时间戳转时间格式(UTC)
    @pytest.mark.parametrize("timestamp", timestamp_data)
    def test_timestamp_utc_datetime(self, timestamp):
        assert xdatetime.get(timestamp, tz=UTC8(hours=0, minutes=0)).format() == arrow.get(timestamp).format("YYYY-MM-DD HH:mm:ss")

    # 时间戳转时间格式(北京时间)
    @pytest.mark.parametrize("timestamp", timestamp_data)
    def test_timestamp_beijing_datetime(self, timestamp):
        assert xdatetime.get(timestamp).format() == arrow.get(timestamp, tzinfo=UTC8()).format("YYYY-MM-DD HH:mm:ss")

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
        assert xdatetime.get(all_datetime_string).format(formatting) == all_datetime_string

    datetime_to_time = [(datetime(2020, 3, 23, 21, 56, 12), "2020-03-23 21:56:12"), (datetime(2020, 3, 23), "2020-03-23 00:00:00")]

    # datetime转时间
    @pytest.mark.parametrize("get_datetime,result", datetime_to_time)
    def test_datetime_to_time(self, get_datetime, result):
        assert xdatetime.get(get_datetime).format() == result

    date_to_time = [(date(2020, 3, 23), "2020-03-23 00:00:00")]

    # date转时间
    @pytest.mark.parametrize("get_date,result", date_to_time)
    def test_date_to_time(self, get_date, result):
        assert xdatetime.get(get_date).format() == result


# 时间模块shape方法
class TestXDateTimeShape(object):
    """
    时间模块的shape方法,进行时间字符串效验
    """
    datetime_or_time = [("2020-03-23 00:00:00", True), (25251425, True), (253698.25, True), ("2020-03-", False), ("english", False), ("我是一个兵", False),
                        ("258741", True), ("2020/03/20T10:09:06.252525+0800", True)]

    # datetime格式效验
    @pytest.mark.parametrize("get_date,result", datetime_or_time)
    def test_datetime_to_shape(self, get_date, result):
        assert xdatetime.shape(get_date) == result
