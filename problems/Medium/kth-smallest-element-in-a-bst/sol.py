from typing import List
from functools import cache

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	@cache
	def size(self, root):
		if not root:
			return 0
		else:
			return 1 + self.size(root.left) + self.size(root.right)

	@cache
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		num_left = self.size(root.left)
		if k == num_left + 1:
			return root.val
		elif k <= num_left:
			return self.kthSmallest(root.left, k)
		else:
			return self.kthSmallest(root.right, k - num_left -1)


print(Solution().kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 4))