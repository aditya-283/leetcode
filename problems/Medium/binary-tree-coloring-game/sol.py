from typing import List
from functools import cache

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def search(self, root, x):
		if not root:
			return None
		if root.val == x:
			return root
		else:
			return self.search(root.left, x) or self.search(root.right, x)

	@cache
	def size(self, root):
		if not root:
			return 0
		return self.size(root.left) + self.size(root.right) + 1


	def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
		node_x = self.search(root, x)
		size_x = self.size(node_x)
		rem = n  - size_x
		if rem > size_x:
			return True
		left = self.size(node_x.left)
		right = self.size(node_x.right)
		if left > right + rem + 1 or right > left + rem + 1:
			return True
		return False