from typing import List
from collections import defaultdict


class UnionFind:
	def __init__(self, elements):
		self.elements = elements
		self.parent = {x: x for x in elements}
		self.rank = {x: 1 for x in elements}

	def find(self, x):
		if x != self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def unionByRank(self, x, y):
		xroot, yroot = self.find(x), self.find(y)

		if xroot == yroot:
			return

		if self.rank[xroot] > self.rank[yroot]:
			self.parent[yroot] = xroot
		elif self.rank[xroot] < self.rank[yroot]:
			self.parent[xroot] = yroot
		else:
			self.parent[yroot] = xroot
			self.rank[xroot] += 1

	# returns a a dictionary mapping each root to all its children. The children include the root itself.
	def enumerate(self):
		d = defaultdict(list)
		for x in self.elements:
			d[self.find(x)].append(x)
		return d


class Solution:
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		name = {email: account[0] for account in accounts for email in account[1:]}
		unionFind = UnionFind(name)
		for account in accounts:
			first = account[1]
			for email in account[1:]:
				unionFind.unionByRank(email, first)

		members = unionFind.enumerate()
		return [[name[k]] + sorted(members[k]) for k in members]


print(Solution().accountsMerge([["David","David0@m.co","David1@m.co"],
								["David","David3@m.co","David4@m.co"],
								["David","David4@m.co","David5@m.co"],
								["David","David2@m.co","David3@m.co"],
								["David","David1@m.co","David2@m.co"]]))