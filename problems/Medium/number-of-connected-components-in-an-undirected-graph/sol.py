from typing import List
from collections import deque, defaultdict

class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		def bfs(s):
			q = deque([s])
			while q:
				top = q.pop()
				for nbr in adjlist[top]:
					if nbr not in discovered:
						adjlist[nbr].remove(top)
						discovered.add(nbr)
						q.appendleft(nbr)


		def get_adjlist(n, edges):
			adjlist = defaultdict(set)
			for n in range(n):
				adjlist[n]

			for v1, v2 in edges:
				adjlist[v1].add(v2)
				adjlist[v2].add(v1)
			return adjlist

		components = 0
		discovered = set()
		adjlist = get_adjlist(n, edges)
		for node in range(n):
			if node not in discovered:
				discovered.add(node)
				bfs(node)
				components += 1
		return components


print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))