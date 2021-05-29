from typing import List
from functools import cache
from collections import defaultdict
from math import inf

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
		seen = defaultdict(int)
		ans = []
		@cache
		def helper(root):
			if not root:
				return 
			else:
				hash = (root.val, helper(root.left), helper(root.right))
				seen[hash] += 1
				if seen[hash] > 1:
					ans.append(root)
					seen[hash] = -inf
				return hash
		helper(root)
		return ans


print(Solution().findDuplicateSubtrees(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4)))))