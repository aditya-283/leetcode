from typing import List
from collections import deque

# Definition for a binary tree node.
class Node:
	def __init__(self, x, children=None):
		self.val = x
		self.children = children

class Codec:
	def serialize(self, root: "Node") -> str:
		"""Encodes a tree to a single string.
		"""
		if not root:
			return ''
		subtreeStrings = [f'({self.serialize(child)})' for child in root.children] if root.children else []
		return f'{root.val}' + (' ' + ' '.join(subtreeStrings) if subtreeStrings else '')
		

	def deserialize(self, data: str) -> "Node":
		"""Decodes your encoded data to tree.
		"""
		if not data:
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

		return Node(rootVal, [self.deserialize(subtreeString) for subtreeString in subtreeStrings])



		

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = Node(2, [Node(1, [Node(.5), Node(1.5)]), Node(3), Node(6, [Node(4), Node(8)])])
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
print(ans.children[2].children[1].val)