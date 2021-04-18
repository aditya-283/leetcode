from typing import List
from collections import defaultdict

class Solution:
	def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
		adjList = [[] for _ in range(n)]
		for edge in connections:
			adjList[edge[0]].append(edge[1])
			adjList[edge[1]].append(edge[0])


		opened = {}
		closed = {}
		parent = {}
		highest_reachable = {v: v for v in range(n)}
		global time
		time = 0
		bridges = set()
		def dfs_visit(v):
			global time
			time += 1
			opened[v] = time
			for nbr in adjList[v]:
				if not nbr in opened and not nbr in closed:
					parent[nbr] = v
					dfs_visit(nbr)
				if nbr in opened and not nbr in closed and nbr != parent[v]:
					highest_reachable[v] = nbr if v not in highest_reachable or opened[nbr] < opened[highest_reachable[v]] else highest_reachable[v]
			for nbr in adjList[v]:
				if nbr in closed and nbr != parent[v] and \
				   ((v not in highest_reachable and nbr in highest_reachable) or 
				   	(nbr in highest_reachable and opened[highest_reachable[nbr]] < opened[highest_reachable[v]])):
					highest_reachable[v] = highest_reachable[nbr] 
			time += 1
			closed[v] = time


		start = connections[0][0]
		parent[start] = -1
		dfs_visit(start)
		for v in range(n):
			for nbr in adjList[v]:
				if not nbr in highest_reachable or opened[highest_reachable[nbr]] > opened[v]:
					if not (v, nbr) in bridges and not (nbr, v) in bridges: 
						bridges.add((v, nbr))
		print(highest_reachable.items())

		return list(bridges)



print(Solution().criticalConnections(7, [[0,1],[2,3],[3,0],[3,4],[4,5],[5,6],[6,4]]))