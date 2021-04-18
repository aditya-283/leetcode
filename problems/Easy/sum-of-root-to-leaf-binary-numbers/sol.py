from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	def sumRootToLeaf(self, root: TreeNode) -> int:
		def getPaths(root):
			if not root:
				return []
			if not root.left and not root.right:
				return [[str(root.val)]]
			else:
				return [[str(root.val)] + path for path in getPaths(root.left) + getPaths(root.right)]
		paths = getPaths(root)
		return sum([int(''.join(path), 2) for path in paths])

print(Solution().sumRootToLeaf(TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))))
