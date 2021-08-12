from collections import deque
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def height(self):
		it = self
		height = 0
		while it:
			it = it.left
			height += 1
		return height


	def __repr__(self):
		return f'TreeNode({self.val}, {self.left}, {self.right})' 


class SpiralSolution:
	def __init__(self, tree):
		self.tree = tree 
		self.levelQueues = [deque() for _ in range(tree.height())]

	def preprocess(self):
		q = deque([(self.tree, 0)])
		while q:
			cur, level = q.pop()
			self.levelQueues[level].append(cur.val)
			if cur.left:
				q.appendleft((cur.left, level+1))
				q.appendleft((cur.right, level+1))
		return

	def traverse(self):
		while self.levelQueues:
			for level in self.levelQueues[:-1]:
				if level:
					print(level.popleft())

			for leaf in self.levelQueues[-1]:
				print(leaf)
			self.levelQueues.pop()

			for level in reversed(self.levelQueues):
				if level:
					print(level.pop())



