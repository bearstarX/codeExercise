# -*- coding: utf-8 -*-#
# ----------------------
# Name: p5-bisect
# Description: bisect管理已排序的序列
# Author: luozelin
# Date: 2022/1/5 0005
# ----------------------

# 　在有序序列中用 bisect 查找某个元素的插入位置

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

def demo(biscet_fn):
	for needle in reversed(NEEDLES):
		position = biscet_fn(HAYSTACK,needle)
		offset = position * ' |'
		print(ROW_FMT.format(needle,position,offset))

# if __name__=='__main__':
# 	if sys.argv[-1] == 'left':
# 		bisect_fn = bisect.bisect_left
# 	else:
# 		bisect_fn = bisect.bisect_right
#
# 	print('DEMO:',bisect_fn.__name__)
# 	print('haystack ->',' '.join('%2d' % n for n in HAYSTACK))
# 	demo(bisect_fn)

# 根据一个分数，找到它所对应的成绩
# def grade(score,breakpoints = [60,70,80,90],grades='FDCBA'):
# 	i = bisect.bisect(breakpoints,score)
# 	return grades[i]
#
# grade_list = [grade(score) for score in [33,99,77,70,89,90,100]]
# print(grade_list)

# insort可以保持有序序列的顺序
import bisect
import random

SIZE = 7

random.seed(1729)	# seed参数一致时，保证每次生成的随机数是一样的

my_list = []
for i in range(SIZE):
	new_item = random.randrange(SIZE*2)
	bisect.insort(my_list,new_item)
	print(my_list)