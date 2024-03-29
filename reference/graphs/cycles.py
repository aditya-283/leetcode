# officially the worst method ever is checking for odd length cycles using BFS
from collections import deque, defaultdict
from typing import List

def isBipartiteBFS(graph: List[List[int]]) -> bool:
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




#Below are the best solutions for bipartite checking. DO NOT CHECK FOR ODD LENGTH CYCLES! STUPID

class SolutionDFS:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		def color_node(u, clr=True):
			if u in color: return color[u] == clr
			else:
				color[u] = clr
				return all(color_node(nbr, not clr) for nbr in graph[u])
		color = {}
		return all(color_node(s) for s in range(len(graph)) if s not in color)


class SolutionUF:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		uf = UnionFind(range(len(graph)))
		for node in graph:
			for nbr in graph[node]:
				if uf.find(node) == uf.find(nbr):
					return False
				uf.union(nbr, graph[node][0])

		return True



# general cycle detection and topo sort

# As a general rule, don't use exceptions for control flow. But also, cycle detection IS an exceptional route for a toposort program
# So the final word is this - if the name of your function is isDAG whose main purpose is to look for cycles, then using exceptions for control flow is considered bad.
# But if you're doing topo sort and the expectation is receiving a DAG and you're required only to take care of that, then using a ValueError for the exceptional cyclic case isn't too bad. 
# Ultimately it does come down to taste and readability a little bit. The convoluted if statements that percolate the -1 from the deep within the recursion to outside, is also not super readable
# Two ways around that - using a stack to avoid recursion entirely and to be able to directly return when you see a cyle
# Use an array of backEdges defined outside, that will store all backedges. If its empty, there were no cycles.

class Solution:
	def topoSort(self, n, edges):
		self.graph = defaultdict(list)
		for u, v in edges:
			self.graph[v].append(u)
			self.graph[u]

		def dfs(s):
			opened.add(s)
			for nbr in self.graph[s]:
				if nbr in opened and nbr not in finished:
					raise ValueError("Detected directed cycle")
				if nbr not in opened:
					dfs(nbr)
			finished.add(s)
			topo.appendleft(s)

		opened = set()
		finished = set()
		topo = deque()
		try: 
			for node in self.graph:
				if node not in opened and node not in finished:
					dfs(node)
		except ValueError:
			return []

		return topo


print(Solution().topoSort(2, [[0,1],[1,0]]))


























