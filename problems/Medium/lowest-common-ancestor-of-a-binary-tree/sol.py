from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		discovered = set()
		parent = {}

		def ancestors(v):
			iter = v
			ancestors = [iter]
			while parent[iter] != -1:
				iter = parent[iter]
				ancestors.append(iter)
			return reversed(ancestors)

		def lastmatch(l1, l2):
			for x, y in zip(l1, l2):
				if x == y:
					match = x
			return match

		def bfs(s):
			q = deque()
			q.appendleft(s)
			parent[s] = -1
			while q:
				top = q.pop()
				if top.left:
					parent[top.left] = top
					q.appendleft(top.left)
				if top.right:
					parent[top.right] = top
					q.appendleft(top.right)

		bfs(root)
		return lastmatch(ancestors(p), ancestors(q))


	def lowestCommonAncestorInefficient(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		def lastmatch(l1, l2):
			for x, y in zip(l1, l2):
				if x == y:
					match = x
			return match

		def dfs(v, x, open):
			left, right = None, None
			if v and v != x:
				left = dfs(v.left, x, open + [v]) 
				right = dfs(v.right, x, open + [v])
			elif v == x:
				return open + [v]
			return left or right

		return lastmatch(dfs(root, p, []), dfs(root, q, []))




tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(Solution().lowestCommonAncestor(tree, tree.left, tree.left.right.right).val)