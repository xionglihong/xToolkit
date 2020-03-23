#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 18:26
# @Author  : 熊利宏
# @project : 字符串模块
# @Email   : xionglihong@163.com
# @File    : xstring.py
# @IDE     : PyCharm
# @REMARKS : 字符串模块的公共功能

# 正则表达式
import re


# 公共功能
class BasicsFunction(object):
    """
    字符串模块的公共功能
    """

    def __init__(self, mark):
        self.__mark = mark

    # 身份证号码处理
    def identity_card(self, *args):
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
