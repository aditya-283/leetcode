from typing import List
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def isSubtreeFrom(self, big, small) -> bool:
		if not small:
			return not big

		if not big:
			return False

		if small.val == big.val:
			return self.isSubtreeFrom(small.left, big.left) and self.isSubtreeFrom(small.right, big.right)
		else:
			return False

	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		if not s:
			return not t
		return self.isSubtreeFrom(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


print(Solution().isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)),
						   TreeNode(4, TreeNode(1), TreeNode(2))))
