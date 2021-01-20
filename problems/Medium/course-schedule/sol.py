from typing import List
from collections import defaultdict, deque

class Solution:
	def edgelist_to_adjlist(self, num_nodes, edgelist):
		adjlist = [[] for _ in range(num_nodes)]
		for edge in edgelist:
			# print(edge)
			adjlist[edge[0]].append(edge[1])
			# print()
		# print('Here: ', str(adjlist))
		return adjlist

	def hasCycle(self, adjlist):
		def dfs_visit(v):
			discovered.add(v)
			for nbr in adjlist[v]:
				if nbr not in discovered and nbr not in finished:
					dfs_visit(nbr)
				elif nbr in discovered:
					back_edges.append((v, nbr))
			finished.add(v)
			discovered.remove(v)

		discovered = set()
		finished = set()
		back_edges = []
		for v in range(len(adjlist)):
			if v not in discovered and v not in finished:
				dfs_visit(v)
		return len(back_edges) > 0


	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		adjlist = self.edgelist_to_adjlist(numCourses, prerequisites)
		return not self.hasCycle(adjlist)



print(Solution().canFinish(2, [[1,0],[0,1]]))