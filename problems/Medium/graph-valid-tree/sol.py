from typing import List

class Set:
	def __init__(self, x):
		self.val = x
		self.rank = 1
		self.parent = x

	def __repr__(self):
		return f'SET:{self.x}'

class UnionFind:
	def __init__(self, lst):
		self.map = {n: Set(n) for n in lst}

	def __repr__(self):
		s = ''
		for elem in self.map:
			s += f'{elem} in {find(self.map[elem])}'


	def union_by_rank(x: Set, y: Set):
		if x.rank == y.rank:
			x.parent = y
			y.rank += 1
		elif x.rank < y.rank:
			x.parent = y
		else:
			y.parent = x

	# path compression
	def find(x: Set):
		if x.parent != x:
			x.parent = self.find(x.parent)
		return x.parent 


	def link(x, y):
		union_by_rank(self.find(self.map[x]), self.find(self.map[y]))

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
    	forest = UnionFind(range(n))
    	print(forest)
    	for edge in edges:
    		link(edge[0], edge[1])

    	print(forest)from typing import List
