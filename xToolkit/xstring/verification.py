#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 10:58
# @Author  : 熊利宏
# @project : 正则表达式校对
# @Email   : xionglihong@163.com
# @File    : verification.py
# @IDE     : PyCharm

# 正则表达式
import re

# 时间模块
import datetime


# 正则表达式校对
class DataProofreading(object):
    """
    进行格式校对，包括身份证，手机号码等
    """

    # 数据效验
    def verified(self, strings, dtype):

        # 判断传来的是否为字符串
        if not isinstance(strings, str):
            return {"code": "0001", "result": False, "msg": "传入的数据类型必须为字符串"}

        # 进行中国大陆身份证效验
        if dtype == "identity":
            """
            暂时只支持效验18位身份证
            """
            # 判断传来的是否为字符串
            if not isinstance(strings, str):
                return {"code": "0001", "result": False, "msg": "传入的数据类型必须为字符串"}

            # 市县编号
            from .xstring_data import area_dict

            # 效验码
            id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]

            # 判断长度
            if len(strings) != 18:
                return {"code": "0001", "result": False, "msg": "身份证长度不合规，长度应该为18位"}

            # 判断格式是否为17位+以为效验
            if not re.match(r"^\d{17}(\d|X|x)$", strings):
                return {"code": "0001", "result": False, "msg": "身份证格式不合格"}

            # 判断生日部分
            try:
                datetime.date(int(strings[6:10]), int(strings[10:12]), int(strings[12:14]))
            except ValueError as ve:
                return {"code": "0001", "result": False, "msg": "身份证生日部分不合格"}

            # 进行效验码判断
            if str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in strings[0:-1]])]) % 11]) != str(strings.upper()[-1]):
                return {"code": "0001", "result": False, "msg": "身份证号码不合格，校验码判断失败"}

            return {"code": "0000",
                    "result": True,
                    "birthday": "{}-{}-{}".format(strings[6:10], strings[10:12], strings[12:14]),  # 生日
                    "gender": "男" if int(strings[-2]) % 2 == 1 else "女",  # 性别
                    "place": "{}省 {}市 {}".format(area_dict.get(strings[0:2] + "0000").rstrip("省"),
                                                 area_dict.get(strings[0:4] + "00", "省直辖行政单位").rstrip("市"),
                                                 area_dict.get(strings[0:6], "部分区域")),  # 省市
                    }
        # 手机号码效验
        elif dtype == "iphone":
            """
            移动：134、135、136、137、138、139、150、151、152、157(TD)、158、159、178(新)、182、184、187、188
            联通：130、131、132、152、155、156、185、186
            电信：133、153、170、173、177、180、181、189、（1349卫通）
            总结起来就是第一位必定为1，第二位必定为3或5或8，其他位置的可以为0 - 9
            使用正则表达式 ^1[3|5|7|8|][0-9]{9}$
            """
            if re.findall("^1[3|5|7|8|][0-9]{9}$", strings):
                return {"code": "0000", "result": True, "msg": ""}
            else:
                return {"code": "0001", "result": False, "msg": "使用正则表达式 ^1[3|5|7|8|][0-9]{9}$"}
        # 浮点型或者整形(正负都可以)
        elif dtype == "float_int":
            if re.findall('(^-?[1-9]\d*\.\d+$)|(^-?0\.\d*[1-9]\d*$)|(^-?[1-9]\d*$)', strings):
                return {"code": "0000", "result": True, "msg": ""}
            else:
                return {"code": "0001", "result": False, "msg": ""}
        # 浮点型(正负都可以)
        elif dtype == "float":
            if re.findall('(^-?[1-9]\d*\.\d+$)|(^-?0\.\d*[1-9]\d*$)', strings):
                return {"code": "0000", "result": True, "msg": ""}
            else:
                return {"code": "0001", "result": False, "msg": ""}
        # 姓名（只含中文）
        elif dtype == "name":
            # 姓名要求为2-5个中文
            if re.findall('^[\u4e00-\u9fa5]{2,5}$', strings):
                return {"code": "0000", "result": True, "msg": ""}
            else:
                return {"code": "0001", "result": False, "msg": "姓名要求为2-5个中文"}
        # 银行卡效验
        elif dtype == "bank":
            # 第一位不能为0,并且15到19位数字
            if re.findall('^[1-9]\d{14,18}$', strings):
                return {"code": "0000", "result": True, "msg": ""}
            else:
                return {"code": "0001", "result": False, "msg": "第一位不能为0,并且15到19位数字"}
        else:
            return {"code": "0001", "result": False, "msg": "dtype 无对应类型"}
