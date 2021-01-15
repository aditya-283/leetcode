from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
		if not inorder or not postorder:
			return None
		root = postorder[-1]
		inorderRootIdx = inorder.index(root)
		return TreeNode(root, 
						self.buildTree(inorder[:inorderRootIdx], postorder[:inorderRootIdx]), 
						self.buildTree(inorder[inorderRootIdx+1:], postorder[inorderRootIdx:-1]))


a = Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
print(a.right.val)