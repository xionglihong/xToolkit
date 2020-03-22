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


# 校验模块
class CheckData(object):

    def __init__(self, mark):
        self.__mark = mark

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
    def is_identity_card(self, *args):
        """
        提供中国大陆身份证验证，暂时只支持效验18位身份证

        mold表示消息类型，为选填
            为空表示不输出错误或正确消息，只输出 True 或者 False，表示格式正确或者错误
            True 输出正确消息，包括出生年月，性别基础信息
            False 输出完整身份证信息，包括市县，出生年月日，性别等信息，但速度比较慢，因为是进行的网络查询
        """
        arg = len(args)

        # 判断返回值类型
        if arg == 0:
            mold = None
        elif arg == 1:
            if args[0] not in [False, True]:
                raise ValueError("传入的值必须为True或者False")
            else:
                mold = args[0]
        else:
            raise ValueError("可以不传值，若传入值，值必须为True或False")

        # 效验码
        id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]

        # 待验证的值必须为字符串
        if not isinstance(self.__mark, str):
            if mold is None:
                return False
            else:
                return {"code": "0001", "msg": "待验证的值必须为字符串", "data": None}

        # 待验证的值长度必须为18位
        if len(self.__mark) != 18:
            if mold is None:
                return False
            else:
                return {"code": "0001", "msg": "待验证的值长度必须为18位", "data": None}

        # 待验证的值格式必须为17位数字+一位数字或者X或者x
        if not re.match(r"^\d{17}(\d|X|x)$", self.__mark):
            if mold is None:
                return False
            else:
                return {"code": "0001", "msg": "待验证的值格式必须为17位数字+一位数字或者X或者x", "data": None}

        # 效验码
        if str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in self.__mark[0:-1]])]) % 11]) != str(self.__mark.upper()[-1]):
            if mold is None:
                return False
            else:
                return {"code": "0001", "msg": "效验码综合验证失败", "data": None}

        # 验证成功
        if mold is None:
            return True
        elif mold is True:
            birthday = "{}-{}-{}".format(self.__mark[6:10], self.__mark[10:12], self.__mark[12:14])  # 生日
            gender = "男" if int(self.__mark[-2]) % 2 == 1 else "女"  # 性别
            return {"code": "0000", "msg": "身份证格式正确", "data": {"birthday": birthday, "gender": gender}}
        elif mold is False:
            return {"code": "0000", "msg": "身份证格式正确", "data": {"msg": "占时还没有找到稳定的接口"}}
