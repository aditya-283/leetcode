from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	@cache
	def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
		if not root1 and not root2:
			return True
		elif not root1 or not root2:
			return False
		else:
			return root1.val == root2.val and ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
									      or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))

