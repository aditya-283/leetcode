from typing import List
from collections import defaultdict, deque

class Solution:
	# def __init__(self):
	# 	self.t = 0
	def edgelist_to_adjlist(self, edgelist):
		adjlist = defaultdict(list)
		for edge in edgelist:
			adjlist[edge[0]].append(edge[1])	

			if edge[1] not in adjlist:
				adjlist[edge[1]] = []			
			
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
		for v in adjlist.keys():
			if v not in discovered and v not in finished:
				dfs_visit(v)
		return len(back_edges) > 0


	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		adjlist = self.edgelist_to_adjlist(prerequisites)
		return not self.hasCycle(adjlist)


	def dfs(self, edgelist):
		global t
		t = 0
		adjlist = self.edgelist_to_adjlist(edgelist)
		visited, parent, start, end = {}, {}, {}, {}
		def dfs_visit(v):
			global t
			visited[v] = 1
			t += 1
			start[v] = t
			for nbr in adjlist[v]:
				if nbr not in visited:
					parent[nbr] = v
					dfs_visit(nbr)
			t += 1
			end[v] = t

		for v in adjlist.keys():
			if v not in visited:
				parent[v] = -1
				dfs_visit(v)
		print('PARENT', str(parent))
		print('START', str(start))
		print('END', str(end))
		return start, end
	def toposort(self, edgelist)


print(Solution().dfs([[1,2],
					  [1,3],
					  [1,4],
					  [3,2],
					  [2,5], 
					  [2,6],
					  [3,6],
					  [3,7]]))