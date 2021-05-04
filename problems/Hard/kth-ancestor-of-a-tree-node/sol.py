from typing import List
from collections import defaultdict
from functools import cache

class TreeAncestor:
	def __init__(self, n: int, parent: List[int]):
		self.parent = parent

	@cache
	def getKthAncestor(self, node: int, k: int) -> int:
		if node == -1 or (node == 0 and k > 0):
			return -1
		if k == 0:
			return node
		elif k == 1:
			return self.parent[node]
		elif not (k & (k-1)):
			return self.getKthAncestor(self.getKthAncestor(node, k//2), k//2)
		else:
			msb = 1 << (k.bit_length()-1)
			return self.getKthAncestor(self.getKthAncestor(node, msb), k - msb)