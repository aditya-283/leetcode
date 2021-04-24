from typing import List
from collections import defaultdict, deque
from itertools import product
import bisect

class UnionFind:
	def __init__(self, elements):
		self.elements = elements
		self.parent = {element: element for element in elements}
		self.rank = {element: 1 for element in elements}

	def __repr__(self):
		return f"PARENTS {self.parent}\nRANKS {self.rank}"

	def find(self, x):
		while self.parent[x] != x:
			x = self.parent[x]
		return self.parent[x]

	def union(self, x, y):
		root_x, root_y = self.find(x), self.find(y)
		if self.rank[root_x] < self.rank[root_y]:
			self.parent[root_x] = root_y
		elif self.rank[root_y] < self.rank[root_x]:
			self.parent[root_y] = root_x
		else:
			self.parent[root_x] = root_y
			self.rank[root_y] += 1

class Solution:
	def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
		syn_word_set = {word for pair in synonyms for word in pair}
		unionFind = UnionFind(syn_word_set)

		for w1, w2 in synonyms:
			unionFind.union(w1, w2)

		group = defaultdict(list)
		for w in syn_word_set:
			bisect.insort(group[unionFind.find(w)], w)

		marked = [w for w in text.split() if w in syn_word_set]
		choices = product(*[group[unionFind.find(w)] for w in marked])
		sentences = []
		for choice in choices:
			lst = deque(choice)
			sentences.append(" ".join([w if w not in syn_word_set else lst.popleft() for w in text.split()]))
		return sentences
