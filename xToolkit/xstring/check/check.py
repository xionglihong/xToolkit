#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 20:52
# @Author  : 熊利宏
# @project : 字符串验证模块
# @Email   : xionglihong@163.com
# @File    : xstring.py
# @IDE     : PyCharm
# @REMARKS : 字符串验证功能

# 正则表达式
import re

# 字符串公共功能
from ..xstring import BasicsFunction

# 基类格式判断
from xToolkit.xtoolkit.judgement import JudgeType


# 校验模块
class CheckData(object):

    def __init__(self, mark):
        self.__mark = mark

        # 基类格式判断
        self.judge = JudgeType

    # 正则表达式验证方法
    def __regular_expression(self, expression):
        """
        正则表达式验证方法
        """
        # 需要验证的字符串
        string = self.__mark

        if re.findall(expression, string):
            return True
        else:
            return False

    # 车牌号
    @property
    def is_car_number(self):
        """
        提供中国大陆车牌号验证

        表达式校验的规则：
            常规车牌号：省份+地区代码+五位数字/大写英文字母（序号位）如：粤B12345。 
                1. 序号位不存在字母I和O防止1、0混淆 
                2. 省份范围：京、津、沪、渝、冀、豫、云、辽、黑、湘、皖、鲁、新、苏、浙、赣、鄂、桂、甘、晋、蒙、陕、吉、闽、贵、粤、青、藏、川、宁、琼。 
                3. 地区代码O为省级公安厅专用车牌 
                4. 地区代码U为省级政府专用车牌 
                5. 地区代码中暂无I

            新能源车牌号：省份简称（1位汉字）+发牌机关代号（1位字母）+序号（6位） 
                1. 小型新能源汽车号牌（序号）的第一位必须使用字母D、F（D代表纯电动新能源汽车，F代表非纯电动新能源汽车），第二位可以使用字母或者数字，后四位必须使用数字。 
                2. 大型新能源汽车号牌（序号）的第六位必须使用字母D、F（D代表纯电动新能源汽车，F代表非纯电动新能源汽车），前五位必须使用数字。 
                3. 序号中英文字母I和O不能使用。 
                4. 省份范围同常规车牌号 
                5. 发牌机关代码暂无I

            警车车牌：车牌最后汉字为警字 
                1. 省份+地区代码+4位数字+警（川A0001警） 
                2. 省份+地区代码+字母+3位数字（川AA001警）字母可选项包括（A、B、C、D） 
                3. 省份范围同常规车牌号 
                4. 地区代码没有I 
                5. 地区代码为O时代表为省级公安厅专用车牌

            领事馆车牌：车牌中包括“使”或“领”字 
                1. 大使馆：三位国家代码（数字）+三位车辆编号（数字）+使 
                2. 领事馆：省份简称+地区代码+四位车辆编号（数字）+领（省份与地区代码可选范围包括：沪A、粤A、川A、云A、桂A、鄂A、闽D、鲁B、陕A、蒙A、蒙E、蒙H、藏A、黑A、辽A、渝A）

            武警车牌：车牌开头包括WJ 
                1. 武警总部车牌：WJ+•（中间点）+四个数字+数字或字母 
                2. 武警地方车牌：WJ+省份简称+四位数字+数字或字母 
                3. 省份范围同常规车牌号 
                4. 其中字母包括（T D S H B X J）

            军用车牌：字头+字头号 +序号组成。 
                1. 字头：大写字母汉语拼音字母，字母包括（VKHBSLJNGCE） 
                2. 字头号：大写英文字母，字母包括（A-D,J-P,R-T,V,Y） 
                3. 序号：5位数字
        """
        expression = "^(([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z](([0-9]{5}[DF])|([DF]([A-HJ-NP-Z0-9])[0-9]{4})))" \
                     "|([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z][A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳使领]))$"

        return self.__regular_expression(expression)

    # 身份证
    @property
    def is_identity_card(self):
        """
        提供中国大陆身份证验证，暂时只支持效验18位身份证
        """
        return BasicsFunction(self.__mark).identity_card()

    # 整形或浮点型
    @property
    def is_int_or_float(self):
        return self.judge.is_timestamp(self.__mark)

    # 时间字符串
    @property
    def is_datetime_string(self):
        return self.judge.is_datetime_string(self.__mark)

    # URL地址
    @property
    def is_url(self):
        expression = "(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"
        return self.__regular_expression(expression)

    # 手机号
    @property
    def is_phone(self):
        """
        第一位为1，一共11位数字几个
        """
        expression = "^1\\d{10}$"
        return self.__regular_expression(expression)

    # 银行卡
    @property
    def is_bank_number(self):
        """
        第一位不能为0,并且13到19位数字
        """
        expression = "^[1-9]\\d{12,18}$"
        return self.__regular_expression(expression)

    # 用户姓名
    @property
    def is_user_name(self):
        """
        姓名要求为2-4个中文
        """
        expression = "^[\u4e00-\u9fa5]{2,4}$"
        return self.__regular_expression(expression)

    # 密码
    @property
    def is_user_password(self):
        """
        包含6-18位字符，必须包含字母与数字，可以包含特殊字符
        """
        expression = "^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z\\W]{6,18}$"
        return self.__regular_expression(expression)

    # 邮箱
    @property
    def is_mailbox(self):
        """
        第一种：只允许英文字母、数字、下划线、英文句号、以及中划线组成
        第二种：名称允许汉字、字母、数字，域名只允许英文域名
        二种中任何一种即可
        """
        expression = "^([a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\\.[a-zA-Z0-9_-]+)+)|([A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\\.[a-zA-Z0-9_-]+)+)$"
        return self.__regular_expression(expression)
