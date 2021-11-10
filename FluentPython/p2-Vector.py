# -*- coding: utf-8 -*-#
# ----------------------
# Name: p2-Vector
# Description: 二维向量-p35实例
# Author: luozelin
# Date: 2021/11/10 0010
# ----------------------

# 二维向量计算公式
# Vector(2,4)+Vector(2,1) = Vector(4,5)

from math import hypot

class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	# 打印类实例对象输出__repr__方法返回值，可以理解为类实例对象的自我介绍
	def __repr__(self):
		return f'Vector({self.x},{self.y})'

	def __abs__(self):
		return hypot(self.x,self.y)

	def __bool__(self):
		return bool(abs(self))

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x,y)

	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)



