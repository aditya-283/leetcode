from typing import List
from collections import deque

# Definition for a binary tree node.
# Definition for a binary tree node.


# Preorder + Inorder works directly only if tree has unique elements. Otherwise it doesn't
# Use BFS and bookkeep the nulls as well

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Codec:
	def serialize(self, root: TreeNode) -> str:
		"""Encodes a tree to a single string.
		"""
		if not root:
			return '_'
		else:
			left_repr = f'({self.serialize(root.left)})' if root.left else '_'
			right_repr = f'({self.serialize(root.right)})' if root.right else '_'
			return f'{root.val} {left_repr} {right_repr}'
		

	def deserialize(self, data: str) -> TreeNode:
		"""Decodes your encoded data to tree.
		"""
		if data[0] == '_':
			return None

		arr = data.split()
		rootVal = arr[0]
		data = ' '.join(arr[1:])
		subtreeStrings = []
		nested = 0
		for i in range(len(data)):
			if not nested and data[i] == '_':
				subtreeStrings.append('_')
			if data[i] == '(':
				nested += 1
				if nested == 1:
					start = i
			if data[i] == ')':
				nested -= 1
				if not nested:
					end = i
					subtreeStrings.append(data[start+1:end])

		return TreeNode(rootVal, self.deserialize(subtreeStrings[0]), self.deserialize(subtreeStrings[1]))
		

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)),  TreeNode(60, TreeNode(40), TreeNode(80)))
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
print(ans.right.left.val)
# print(ans.children[2].children[1].val)
