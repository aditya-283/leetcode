from typing import List
from collections import deque


# Definition for a Node.
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

	def __repr__(self):
		return f'NODE [val: {self.val}, neighbors: {[nbr.val for nbr in self.neighbors]}]'



class Solution:
	def graphToAdjList(self, start_node):
		s = deque()
		visited = set()
		adjList = {}
		s.append(start_node)
		while s:
			top = s.pop()
			adjList[top.val] = [nbr.val for nbr in top.neighbors]
			visited.add(top.val)
			for nbr in top.neighbors:
				if nbr.val not in visited:
					s.append(nbr)
		return adjList

	def adjListToGraph(self, adjList, start_value):
		nodes = {val: Node(val) for val in adjList.keys()}
		for val in adjList:
			nodes[val].neighbors = [nodes[nbr] for nbr in adjList[val]]
		return nodes[start_value]

	def cloneGraph(self, node: Node) -> Node:
		if not node:
			return None
		adjList = self.graphToAdjList(start_node=node)
		return self.adjListToGraph(adjList=adjList, start_value=node.val)


# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# a.neighbors = [b, d]
# b.neighbors = [a, c]
# c.neighbors = [b, d]
# d.neighbors = [a, c]
# lst = Solution().graphToAdjList(a)
# print(Solution().adjListToGraph(lst, 1).neighbors[0].neighbors[1].neighbors[1])

a = Node(1)
a.neighbors = []
lst = Solution().graphToAdjList(a)
print(Solution().adjListToGraph(lst, 1))


