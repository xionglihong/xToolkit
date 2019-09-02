#!/usr/bin/env python
# encoding: utf-8
"""
@author: 熊利宏
@email:xionglihong@163.com
@phone：15172383635
@project: X工具集->时间库
@file: __init__.py.py
@time: 2019-05-15 下午9:27
"""
# 此处用于引入arrow，使得可以直接调用arrow成员
from arrow.arrow import Arrow
from arrow.factory import ArrowFactory
from arrow.api import get, now, utcnow

# 判断时间格式是否正确
from .expansions import shape
# 时间起止区间
from .expansions import start_and_end
# 星期列表的字典
from .expansions import get_week_dict
# 返回年龄
from .expansions import get_age_date
# 返回日期段区间
from .expansions import get_interval
# 判断时间是否在区间中
from .expansions import judge_time_range
