from typing import List
from collections import defaultdict, deque

class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		adjlist = defaultdict(list)
		for (var1, var2), value in zip(equations, values):
			adjlist[var1].append((var2, 1/value))
			adjlist[var2].append((var1, value))



		visited = set()
		ratios = {}
		roots = {}
		def bfs(root):
			roots[root] = root
			ratios[root] = {}
			ratios[root][root] = 1
			q = deque([(root, 1, 0)])
			visited.add(root)
			while q:
				cur, acc, par = q.pop()
				ratios[root][cur] = acc
				roots[cur] = root
				for nbr, weight in adjlist[cur]:
					if nbr not in visited:
						q.appendleft((nbr, acc*weight, cur))
						visited.add(nbr)
					elif nbr != par and nbr in ratios[root] and acc*weight != ratios[root][nbr]:
						ratios[root][nbr] = -1  # bad cycle detected. if acc*weight == ratios[root][nbr] then its an allowed cycle


		for node in adjlist:
			if node not in visited:
				bfs(node)

		ans = []
		for u, v in queries:
			if u not in roots or v not in roots:
				ans.append(float(-1))
			elif roots[u] != roots[v]: # belong to different components
				ans.append(float(-1))
			else:
				root = roots[u]
				x = ratios[root][u] # u = x.root
				y = ratios[root][v] # v = y.root
				ans.append(x/y)
		return ans

print(Solution().calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))