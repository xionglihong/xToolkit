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

    # 进行中国大陆身份证效验
    def identity(self, strings):
        """
        暂时只支持效验18位身份证
        """
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
            return {"code": "0002", "result": False, "msg": "身份证格式不合格"}

        # 判断生日部分
        try:
            datetime.date(int(strings[6:10]), int(strings[10:12]), int(strings[12:14]))
        except ValueError as ve:
            return {"code": "0004", "result": False, "msg": "身份证生日部分不合格"}

        # 进行效验码判断
        if str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in strings[0:-1]])]) % 11]) != str(strings.upper()[-1]):
            return {"code": "0005", "result": False, "msg": "身份证号码不合格，校验码判断失败"}

        return {"code": "0000",
                "result": True,
                "birthday": "{}-{}-{}".format(strings[6:10], strings[10:12], strings[12:14]),  # 生日
                "gender": "男" if int(strings[-2]) % 2 == 1 else "女",  # 性别
                "place": "{}省 {}市 {}".format(area_dict.get(strings[0:2] + "0000").rstrip("省"),
                                             area_dict.get(strings[0:4] + "00", "省直辖行政单位").rstrip("市"),
                                             area_dict.get(strings[0:6], "部分区域")),  # 省市
                }

    # 手机号码效验
    def cellphone(self, strings):
        # 移动：134、135、136、137、138、139、150、151、152、157(TD)、158、159、178(新)、182、184、187、188
        # 联通：130、131、132、152、155、156、185、186
        # 电信：133、153、170、173、177、180、181、189、（1349卫通）
        # 总结起来就是第一位必定为1，第二位必定为3或5或8，其他位置的可以为0 - 9
        # 使用正则表达式 ^1[3|5|7|8|][0-9]{9}$
        if re.findall("^1[3|5|7|8|][0-9]{9}$", strings):
            return True
        else:
            return False

    # 数字效验
    def figure(self, strings, mold=1):
        """
        Python 中已经有效验整数的方法 isdigit，只能效验整数
        此方法新增其他的一些数字效验
        mole的值为：
        1.代表 浮点型或者整形(正负都可以)
        2.代表 浮点型(正负都可以)
        """
        # 浮点型或者整形(正负都可以)
        if mold == 1:
            return True if re.findall('(^-?[1-9]\d*.\d*$)|(^-?0.\d*[1-9]\d*$)|(^-?[1-9]\d*$)', strings) else False
        # 浮点型(正负都可以)
        elif mold == 2:
            return True if re.findall('(^-?[1-9]\d*.\d*$)|(^-?0.\d*[1-9]\d*$)', strings) else False
        else:
            return {"code": "0000", "msg": "mole 类型错误"}

    # 汉字效验
    def characters(self, strings, mold=1):
        """
        进行汉字效验
        mole的值为：
        1.代表 只含中文
        """
        # 只含中文
        if mold in [1, "name"]:
            return True if re.findall('^[\u4E00-\u9FA5]+$', strings) else False
        else:
            return {"code": "0000", "msg": "mole 类型错误"}
