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

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]


if __name__=='__main__':
	obj = FrenchDeck()
	print(f'查看卡牌当中的某一个牌{obj.__getitem__(1)}')
	print(f'查看所有的卡牌：{obj._cards}')
	print(f'查看某一个元组对象中的值:{obj.__getitem__(1).rank}')