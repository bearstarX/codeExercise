# -*- coding: utf-8 -*-#
# ----------------------
# Name: p4-Namedtuple
# Description: 具名元组
# Author: luozelin
# Date: 2022/1/4 0004
# ----------------------

from collections import namedtuple

# 创建具名元组类
City = namedtuple('MyCity','name country population coordinates')
tokyo = City('Tokyo','JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[0])

# 自有属性
print(City._fields)