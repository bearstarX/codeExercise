# -*- coding: utf-8 -*-#
# -----------------------
# Name: __str__
# Description:  返回一个对象的描述信息
# Author: luozelin
# Date: 2021/11/11
# -----------------------

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 当print时调用对象的__str__，打印__str__函数中的返回数据
    def __str__(self):
        return f'名字是{self.name},年龄是{self.age}'

tom = Cat("Tom",30)
print(tom)