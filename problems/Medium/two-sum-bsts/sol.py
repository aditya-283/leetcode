from typing import List
from bisect import bisect_left

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	def toList(self, root):
		if not root:
			return []
		else:
			return self.toList(root.left) + [root.val] + self.toList(root.right)

	def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
		first = self.toList(root1)
		second = set(self.toList(root2))
		for num in first:
			if (target - num) in second:
				return True
		return False

print(Solution().twoSumBSTs(TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(1, TreeNode(0), TreeNode(3)), 5))
