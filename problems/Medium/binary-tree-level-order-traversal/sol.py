from typing import List

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def height(self, root):
		if not root:
			return 0
		return 1 + max(self.height(root.left), self.height(root.right))

	def levelOrderHelper(self, root, depth, levels):		
		if root:
			levels[depth].append(root.val)
			self.levelOrderHelper(root.left, depth+1, levels)
			self.levelOrderHelper(root.right, depth+1, levels)

	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		levels = [[] for _ in range(self.height(root))]
		self.levelOrderHelper(root, 0, levels)
		return levels

class Solution2:
	def levelOrderHelper(self, root, depth, levels):		
		if root:
			if depth + 1 > len(levels):
				levels.append([root.val])
			else:
				levels[depth].append(root.val)
			self.levelOrderHelper(root.left, depth+1, levels)
			self.levelOrderHelper(root.right, depth+1, levels)

	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		levels = []
		self.levelOrderHelper(root, 0, levels)
		return levels

print(Solution1().levelOrder(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))
print(Solution2().levelOrder(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))
