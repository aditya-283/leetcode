from typing import List
from functools import reduce
from collections import defaultdict

class UnionFind:
	def __init__(self, elements): #elements should ideally be a list of ids, data can be stored against these ids if needed.
		self.elements = elements
		self.parent = {elem:elem for elem in elements}
		self.rank = {elem: 0 for elem in elements}

	def union(self, elem1, elem2):
		root1, root2 = self.find(elem1), self.find(elem2)
		if root1 == root2:
			return root1
		if self.rank[root1] > self.rank[root2]:
			self.parent[root2] = root1
			return root1
		elif self.rank[root2] > self.rank[root1]:
			self.parent[root1] = root2
			return root2
		else:
			self.rank[root1] += 1
			self.parent[root2] = root1
			return root1

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def components(self):
		comps = defaultdict(list)
		for elem in self.elements:
			comps[self.find(elem)].append(elem)
		return comps

	def __repr__(self):
		return f"PARENTS {self.parent}\nRANKS {self.rank}"


class Solution:
	def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
		graph = defaultdict(list)
		for f, t in dislikes:
			graph[f].append(t)
			graph[t].append(f)

		uf = UnionFind(range(1, N+1))
		for node in graph:
			for nbr in graph[node]:
				if uf.find(node) == uf.find(nbr):
					return False
				uf.union(nbr, graph[node][0])

		return True


print(Solution().possibleBipartition(10, [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]))