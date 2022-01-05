# -*- coding: utf-8 -*-#
# ----------------------
# Name: p3-Descartes
# Description: 笛卡尔积算法
# Author: luozelin
# Date: 2021/12/29 0029
# ----------------------

# 如果你需要一个列表，列表里是 3 种不同尺寸的 T 恤衫，每个尺寸都有2 个颜色，列表里有 6 种组合

t_sizes = ['small','middle','large']
t_colors = ['black','white']
t_list = [(t_size,t_color) for t_size in t_sizes for t_color in t_colors]

print(t_list)