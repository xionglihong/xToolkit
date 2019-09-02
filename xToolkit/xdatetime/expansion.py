#!/usr/bin/env python
# encoding: utf-8
"""
@author: 熊利宏
@email:xionglihong@163.com
@phone：15172383635
@project: xToolkit
@file: expansion.py
@time: 2019-05-15 下午9:55
"""

import time
import arrow


class XDateTime(object):
    """
    日期时间常用功能
    """

    @classmethod
    def shape(self, date, *args, **kwargs):
        """
        判断是否为日期格式,如果格式正确返回True,反之返回False.
        """
        try:
            time.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False

    @classmethod
    def start_and_end(self, genre, space, *args, **kwargs):
        """
        计算指定时间段的第一天和最后一天
        genre:"M"代表月,"Y"代表年
        space: 代表间距　正数代表以后,负数代表以前,绝对值必须为正整数
        返回值为列表

        默认返回值：
        本月的第一天和最后一天的列表,比如[2019-05-01,2019-05-31]
        """
        # 如果类型为月
        if genre == "M":
            # 指定月第一天
            start = eval("""arrow.now().shift(months={}).format("YYYY-MM-01")""".format(space))
            # 指定月的最后一天
            end = eval("""arrow.get("{}").shift(months=1).shift(days=-1).format("YYYY-MM-DD")""".format(start))

            return [start, end]
        # 如果类型为年
        elif genre == "Y":
            # 指定年第一天
            start = eval("""arrow.now().shift(years={}).format("YYYY-01-01")""".format(space))
            # 指定年的最后一天
            end = eval("""arrow.get("{}").shift(years=1).shift(days=-1).format("YYYY-MM-DD")""".format(start))

            return [start, end]
        # 类型的值只能是M或者Y
        else:
            raise RuntimeError('genre is M or Y')

    @classmethod
    def get_week_dict(self, start, end, *args, **kwargs):
        """
        start: 开始时间,时间格式为
        end: 结束时间
        返回值以星期为键,值为日期列表的字典
        """
        # 开始时间
        start = arrow.get(start)
        # 结束时间
        ent = arrow.get(end)

        # 初始化返回的字典
        week_dict = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}

        # 时间间距
        section = abs((ent - start).days)

        # 循环把结果添加到字典中
        for key in range(section + 1):
            week_dict[start.shift(days=key).format("d")].append(start.shift(days=key).format("YYYY-MM-DD"))

        return week_dict

    @classmethod
    def get_age_date(self, data, types, *args, **kwargs):
        """
        计算岁数,传入出生日期,返回年龄
        """
        # 出生日期
        start = arrow.get(data)
        # 当前日期
        end = arrow.now()
        # 计算年龄
        age = end - start

        # 返回年
        if types == "years":
            return age.days // 365
        # 返回日
        if types == "days":
            return age.days

    @classmethod
    def get_interval(self, start, end, *args, **kwargs):
        """
        输入开始日期，结束日期，返回区间内每个月的开始日期和结束日期
        """
        # 如果开始日期小于结束日期，就对调开始与结束日期
        if (arrow.get(start) - arrow.get(end)).days > 0:
            start, end = end, start

        # 计算有多少个月
        month_date = (arrow.get(start).year - arrow.get(end).year) * 12 + (arrow.get(start).month - arrow.get(end).month)

        result = []
        for key in range(abs(month_date) + 1):
            # 开始时间
            starts = eval("""arrow.get("{}").shift(months={}).format("YYYY-MM-01")""".format(start, key))
            # 结束时间
            end = eval("""arrow.get("{}").shift(months=1).shift(days=-1).format("YYYY-MM-DD")""".format(starts))

            result.append([starts, end])

        return result

    @classmethod
    def judge_time_range(cls, section, dot, *args, **kwargs):
        """
        判断时间是否在时间区间中
        section 是一个列表对象，列表中为二个值，第一个为区间开始时间，第二个区间结束时间，格式都为年月日时分秒
        dot 为一个时间点 时间格式为年月日时分秒
        此方法用来判断dot是否在section区间中
        """
        # 获取验证时间点
        dots = time.mktime(time.strptime(dot, "%Y-%m-%d %H:%M:%S"))

        # 计算是否在时间区间中
        if dots - time.mktime(time.strptime(section[0], "%Y-%m-%d %H:%M:%S")) >= 0 and time.mktime(time.strptime(section[1], "%Y-%m-%d %H:%M:%S")) - dots >= 0:
            return True
        else:
            return False
