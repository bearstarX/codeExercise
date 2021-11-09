# -*- coding: utf-8 -*-#
# ----------------------
# Name: p1
# Description: 一摞卡片-p29实例
# Author: luozelin
# Date: 2021/11/8 0008
# ----------------------

import collections

Card = collections.namedtuple('Card',['rank','suit'])	# 命名元组

class FrenchDeck:
	# 扑克点数
	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	# 花色
	suits = 'spades diamonds clubs hearts'.split(' ')


	def __init__(self):
		# 如下代码为self._cards简写
		# self._cards = []
		# for suit in self.suits:
		# 	for rank in self.ranks:
		# 		self._cards.append(Card(rank,suit))
		self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

	def __len__(self):	# 可以通过len(FrenchDeck)获取长度
		return len(self._cards)

	def __getitem__(self, position):	# 可以通过索引获取指定纸牌,也可以迭代
		return self._cards[position]

# 卡牌排序
# {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
	'''通过Card对象进行花色计算,升序排序'''
	rank_value = FrenchDeck.ranks.index(card.rank)	# FrenchDeck隐式地继承了object类
	return rank_value * len(suit_values) + suit_values[card.suit]


if __name__=='__main__':
	obj = FrenchDeck()
	print(f'查看卡牌当中的某一个牌{obj.__getitem__(1)}')
	print(f'查看所有的卡牌：{obj._cards}')
	print(f'查看某一个元组对象中的值:{obj.__getitem__(1).rank}')	# 对应特性__getitem__
	print(f'总共有{len(obj)}张牌')	# 对应特性__len__
	print(f'通过切片获取纸牌【{obj[:3]}】')	# 对应特性__getitem__
	# 升序排序（将obj的每个card对象传参给spades_high函数进行运算，然后生成一个升序排序的card列表）
	for card in sorted(obj,key=spades_high):
		print(card)
