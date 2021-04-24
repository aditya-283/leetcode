from typing import List
from collections import defaultdict
from math import inf

class Solution:
	def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
		adjlist = defaultdict(list)
		for edge in connections:
			adjlist[edge[0]].append(edge[1])
			adjlist[edge[1]].append(edge[0])


		def dfs_bridges(time, node, parent):
			disc[node] = time
			low[node] = time
			for nbr in adjlist[node]:
				if nbr == parent:
					continue

				if disc[nbr] != inf:
					low[node] = min(low[node], disc[nbr])
				if disc[nbr] == inf:
					dfs_bridges(time + 1, nbr, node)
					if low[nbr] > disc[node]:
						bridges.append((node, nbr))
					else:
						low[node] = min(low[node], low[nbr])

		n = len(adjlist)
		disc = [inf] * n
		low  = [inf] * n
		bridges = []
		dfs_bridges(0, 1, -1)
		return bridges


print(Solution().criticalConnections(7, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]))