# -*- coding: utf-8 -*-#
# ----------------------
# Name: p6-deque
# Description: 双向队列
# Author: luozelin
# Date: 2022/1/5 0005
# ----------------------

from collections import deque

dq = deque(range(10),maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11,22,33])
print(dq)

dq.extendleft([10,20,30,40])
print(dq)

