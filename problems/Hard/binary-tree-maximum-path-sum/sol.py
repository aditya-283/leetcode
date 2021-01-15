from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def __init__(self):
		self.mss = defaultdict(lambda x:-1)
		self.mpsf = defaultdict(lambda x: -1)

	def maxSegmentSum(self, root):
		if root in self.mss:
			return self.mss[root]
		if not root:
			return 0
		else:
			self.mss[root] = root.val + max(0, self.maxSegmentSum(root.left), self.maxSegmentSum(root.right))
			return self.mss[root]

	def maxPathSumFrom(self, root):
		if root in self.mpsf:
			return self.mpsf[root]
		if not root:
			return 0
		else:
			self.mpsf[root] = root.val + max(0, self.maxSegmentSum(root.left)) + max(0, self.maxSegmentSum(root.right))
			return self.mpsf[root]


	def maxPathSum(self, root: TreeNode) -> int:
		if not root:
			return -1*float('inf')
		else:
			return max(self.maxPathSum(root.left), 
					   self.maxPathSum(root.right), 
					   self.maxPathSumFrom(root))


print(Solution().maxPathSum(TreeNode(-10)))