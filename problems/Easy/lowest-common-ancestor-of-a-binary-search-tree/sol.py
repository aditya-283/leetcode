from typing import List

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x, left=None, right=None):
		self.val = x
		self.left = left
		self.right = right

class Solution:
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		if p == q:
			return p
		elif p.val <= root.val <= q.val or p.val >= root.val >= q.val:
			return root
		elif p.val < root.val:
			return self.lowestCommonAncestor(root.left, p, q)
		else:
			return self.lowestCommonAncestor(root.right, p, q)


tree =	TreeNode(6,
			TreeNode(2, 
						TreeNode(0),
						TreeNode(4, 
									TreeNode(3),
									TreeNode(5))),
			TreeNode(8, 
						TreeNode(7),
						TreeNode(9)))
p = tree.left
q = tree.left.right
# print(p.val, q.val)
print(Solution().lowestCommonAncestor(tree, p, q).val)