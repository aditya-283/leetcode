from typing import List

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
		if not root:
			return 0
		return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + (root.val if low <= root.val <= high else 0)  


print(Solution().rangeSumBST(TreeNode(1, TreeNode(2))))