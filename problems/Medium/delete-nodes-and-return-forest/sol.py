from typing import List

class Solution:
	def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
		forest = []
		to_delete = set(to_delete)
		def delNodesRec(root):
			if not root: return None
			root.left = delNodesRec(root.left)
			root.right = delNodesRec(root.right)
			if root.val in to_delete:
				if root.left: forest.append(root.left)
				if root.right: forest.append(root.right)
				return None
			else: return root
		if delNodesRec(root): forest.append(root)
		return forest