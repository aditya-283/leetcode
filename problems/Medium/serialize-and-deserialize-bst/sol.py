from typing import List
from collections import deque

# class TreeNode:
# 	def __init__(self, val=0, left=None, right=None):
# 		self.val = val
# 		self.left = left
# 		self.right = right


class Codec:
	def serialize(self, root: TreeNode) -> str:
		"""Encodes a tree to a single string.
		"""
		def preorder(root, acc):
			if not root:
				return
			acc.append(str(root.val))
			preorder(root.left, acc)
			preorder(root.right, acc)

		def inorder(root, acc):
			if not root:
				return
			inorder(root.left, acc)
			acc.append(str(root.val))
			inorder(root.right, acc)

		preorder_arr, inorder_arr = [], []
		preorder(root, preorder_arr), inorder(root, inorder_arr)
		return ' '.join(preorder_arr) + '#' + ' '.join(inorder_arr)


	def deserialize(self, data: str) -> TreeNode:
		"""Decodes your encoded data to tree.
		"""

		def deserializeFromOrderings(preorder, inorder):
			if not preorder:
				return None
			root = preorder[0]
			rootIdx = inorder.index(root)
			leftSubtreeSize = rootIdx
			return TreeNode(root, deserializeFromOrderings(preorder[1:leftSubtreeSize+1], inorder[:rootIdx]), 
								  deserializeFromOrderings(preorder[leftSubtreeSize+1:], inorder[rootIdx+1:]))

		if not data:
			return None

		orderings = data.split('#')
		if len(orderings) != 2:
			print('Malformed input!')

		preorder = [int(x) for x in orderings[0].split()]
		inorder = [int(x) for x in orderings[1].split()] 

		return deserializeFromOrderings(preorder, inorder) 


ser = Codec()
deser = Codec()
root = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)),  TreeNode(60, TreeNode(40), TreeNode(80)))
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
print(ans.right.left.val)