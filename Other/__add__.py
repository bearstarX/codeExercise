# -*- coding: utf-8 -*-#
# -----------------------
# Name: __add__
# Description:  运算符重写
# Author: luozelin
# Date: 2021/11/11
# -----------------------

class Person:
    def __init__(self,num):
        self.num = num

    # 运算符重载
    def __add__(self, other):
        return Person(self.num+other.num)

    def __str__(self):
        return f"num={str(self.num)}"

per1 = Person(1)
per2 = Person(2)

print(per1+per2)    # per1.__add__(per2)
print(per1)
print(per2)