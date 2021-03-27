# Definition for a binary tree node.
from typing import List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def binaryTreePaths(self, root: TreeNode) -> List[str]:
		if not root.right and not root.left: 
			return [f'{root.val}']

		childPaths = []
		if root.right:
			childPaths.extend(self.binaryTreePaths(root.right))
		if root.left:
			childPaths.extend(self.binaryTreePaths(root.left))
		return [f'{root.val}->{path}' for path in childPaths]


print(Solution().binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))