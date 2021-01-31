from typing import List

# Definition for a Node.
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	# def __repr__(self):
		# return f'{self.val}-{self.right}'

class Solution:
	def treeToDoublyList(self, root: Node) -> Node:
		if not root:
			return None

		if root.right:
			rightList = self.treeToDoublyList(root.right)
			root.right = rightList
			rightmost = rightList.left
			rightList.left = root
		else:
			rightmost = root

		if root.left:
			leftList = self.treeToDoublyList(root.left)
			leftList.left.right = root
			root.left = leftList.left
			leftmost = leftList
		else:
			leftmost = root

		leftmost.left = rightmost
		rightmost.right = leftmost
		return leftmost


