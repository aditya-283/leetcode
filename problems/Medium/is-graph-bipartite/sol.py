from typing import List
from collections import deque

class Solution:
	def isBipartiteBFS(self, graph: List[List[int]]) -> bool:
		def bfsContainsOddCycle(s, step):
			q = deque()
			q.appendleft((s, 0))
			disc.add(s)
			dist[s] = 0
			while q:
				cur, step = q.pop()
				step += 1
				for nbr in graph[cur]:
					if nbr not in disc:
						disc.add(nbr)
						dist[nbr] = step
						parent[nbr] = cur
						q.appendleft((nbr, step))
					elif nbr != parent[cur]:
						print(cur, nbr)
						cycleLen = dist[nbr] + dist[cur] + 1
						if cycleLen % 2:
							print(f'Detected cycle due to edge {cur}-{nbr} with starting node {s}')
							return True
			return False

		disc = set()
		parent = {}
		dist = {}
		return not any(bfsContainsOddCycle(i, 0) for i in range(len(graph)) if i not in disc)


	def isBipartite(self, graph: List[List[int]]) -> bool:
		color = {}
		def startColoring(s):
			color[s] = 1
			while True:
				changed = 0
				for node in range(len(graph)):
					nbr_colors = [color[nbr] for nbr in graph[node] if nbr in color]
					if len(set(nbr_colors)) >= 2 or (len(set(nbr_colors)) == 1 and node in color and color[node] == nbr_colors[0]):
						return False
					if node in color:
						for nbr in graph[node]:
							if nbr not in color:
								color[nbr] = not color[node]
								changed += 1
					elif len(nbr_colors) == 1:
						for nbr in graph[node]:
							if nbr not in color:
								color[nbr] = nbr_colors[0]
								changed += 1
						color[node] = not nbr_colors[0]
						changed += 1

				if not changed or len(color) == len(graph):
					break

			return True

		return all(startColoring(s) for s in range(len(graph)) if s not in color)



	


print(Solution().isBipartite([[4],[],[4],[4],[0,2,3]]))

