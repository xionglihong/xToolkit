#!/usr/bin/env python
# encoding: utf-8
"""
@author: 熊利宏
@email:xionglihong@163.com
@phone：15172383635
@project: xToolkit
@file: expansions.py
@time: 2019-05-19 下午8:56
"""
import arrow
from .expansion import XDateTime


# 查询格式
def shape(date, *args, **kwargs):
    """
    判断是否为日期格式,如果格式正确返回True,反之返回False.
    """
    return XDateTime.shape(date, *args, **kwargs)


# 查询日期区间
def start_and_end(genre="M", space=0, *args, **kwargs):
    """
    计算指定时间段的第一天和最后一天
    genre:"M"代表月,"Y"代表年
    space: 代表间距　正数代表以后,负数代表以前,绝对值必须为正整数
    返回值为列表

    默认返回值：
    本月的第一天和最后一天的列表,比如[2019-05-01,2019-05-31]
    """
    return XDateTime.start_and_end(genre, space, *args, **kwargs)


# 获取星期列表
def get_week_dict(start=arrow.now(), end=arrow.now(), *args, **kwargs):
    """
    start: 开始时间
    end: 结束时间
    返回值以星期为键,值为日期列表的字典
    """
    return XDateTime.get_week_dict(start=start, end=end, *args, **kwargs)


# 获取年龄
def get_age_date(data=arrow.now(), types="years", *args, **kwargs):
    """
    data :输入出生日期
    types :返回类型（years返回年,days返回为日）
    返回值：返回年龄
    """
    return XDateTime.get_age_date(data=data, types=types, *args, **kwargs)


# 获取日期段区间
def get_interval(start=arrow.now().format("YYYY-MM-DD"), end=arrow.now().format("YYYY-MM-DD"), *args, **kwargs):
    """
    输入开始日期，结束日期，返回区间内每个月的开始日期和结束日期
    start: 开始时间
    end: 结束时间
    返回值为日期区间的列表,二维列表
    """
    return XDateTime.get_interval(start=start, end=end, *args, **kwargs)


# 判断时间是否在区间中
def judge_time_range(section=['1971-01-01 00:00:00', '2038-12-31 23:59:59'], dot="2039-08-30 00:00:00", *args, **kwargs):
    """
    判断时间是否在时间区间中
    section 是一个列表对象，列表中为二个值，第一个为区间开始时间，第二个区间结束时间，格式都为年月日时分秒
    dot 为一个时间点 时间格式为年月日时分秒
    此方法用来判断dot是否在section区间中

    时间格式：2019-09-02 21:32:55
    """
    return XDateTime.judge_time_range(section=section, dot=dot, *args, **kwargs)
