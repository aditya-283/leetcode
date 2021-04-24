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