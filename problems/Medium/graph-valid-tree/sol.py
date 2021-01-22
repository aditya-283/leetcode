from typing import List
from collections import defaultdict, deque

class Set:
	def __init__(self, x):
		self.val = x
		self.rank = 1
		self.parent = self

	def __repr__(self):
		return f'SET[repr:{self.val}, rank:{self.rank}]'

class UnionFind:
	def __init__(self, lst):
		self.map = {n: Set(n) for n in lst}

	def __repr__(self):
		str = ''
		sets = defaultdict(list)
		for elem, value in self.map.items():
			sets[self.findSet(value).val].append(elem)
		for s in sets:
			str += f'{self.find(s)} : {sets[s]}\n'

		return str

	def union_by_rank(self, x: Set, y: Set):
		if x.rank == y.rank:
			x.parent = y
			y.rank += 1
		elif x.rank < y.rank:
			x.parent = y
		else:
			y.parent = x

	# path compression
	def findSet(self, x: Set):
		if x.parent != x:
			x.parent = self.findSet(x.parent)
		return x.parent 

	## user facing 
	def find(self, x):
		return self.findSet(self.map[x])

	def link(self, x, y):
		self.union_by_rank(self.find(x), self.find(y))

class Solution:
	def validTree(self, n, edges):
		if len(edges) != n-1:
			print('here')
			return False

		if n == 1:
			return True
			
		adjlist = defaultdict(list)
		for v1, v2 in edges:
			adjlist[v1].append(v2)
			adjlist[v2].append(v1)

		def hasCycleBFS(s):
			discovered = set()
			parent = {}
			q = deque()
			q.appendleft(s)
			discovered.add(s)
			parent[s] = -1
			while q:
				top = q.pop()
				for nbr in adjlist[top]:
					if nbr != parent[top]:
						if nbr not in discovered:
							parent[nbr] = top
							discovered.add(nbr)
							q.appendleft(nbr)
						else:
							# print(nbr)
							return False
			return True

		return hasCycleBFS(edges[0][0])


	def validTreeUnionFind(self, n: int, edges: List[List[int]]) -> bool:
		forest = UnionFind(range(n))
		print(forest)
		if len(edges) != n-1:
			return False

		for v1, v2  in edges:
			if forest.find(v1) == forest.find(v2):
				print(forest)
				return False
			forest.link(v1, v2)
		print(forest)

		return True





# print(Solution().validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(Solution().validTree(5, [[0,1], [1,2], [2,3], [1,3]]))

