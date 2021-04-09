from typing import List

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return f'{self.val}'
		
class Solution:
	def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
		def traverse(root):
			if not root:
				return
			if root.left:
				depth[root.left] = depth[root] + 1
			if root.right:
				depth[root.right] = depth[root] + 1
			traverse(root.left)
			traverse(root.right)

		def lca(root, nodes):
			if not root:
				return None

			if root in nodes:
				return root

			left = lca(root.left, nodes)
			right = lca(root.right, nodes)
			if left and right:
				return root
			else:
				return left or right

		depth = {}
		depth[root] = 0
		traverse(root)
		max_depth = max(depth.values())
		deepest = [x for x in depth.keys() if depth[x] == max_depth]
		return lca(root, deepest)

print(Solution().subtreeWithAllDeepest(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))))