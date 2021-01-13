from typing import List

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def greatest(self, root: TreeNode):
		if root and not root.right:
			return root.val
		else:
			return self.greatest(root.right)

	def least(self, root: TreeNode):
		if not root.left:
			return root.val
		else:
			return self.least(root.left)

	def isValidBST(self, root: TreeNode) -> bool:
		if not root:
			return True
		else: 
			rootValCheck = True
			if root.left:
				rootValCheck = rootValCheck and self.greatest(root.left) < root.val
			if root.right:
				rootValCheck = rootValCheck and self.least(root.right) > root.val
			return self.isValidBST(root.left) and self.isValidBST(root.right) and rootValCheck

tree = TreeNode(2, TreeNode(1, TreeNode(0.5), TreeNode(2)), TreeNode(3))
print(Solution().isValidBST(tree))